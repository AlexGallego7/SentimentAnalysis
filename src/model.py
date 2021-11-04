""" Machine Learning model to predict SA"""
import pickle
import re

import nltk
import numpy as np
import pandas as pd
from gensim.models import Word2Vec
from keras.callbacks import EarlyStopping, ReduceLROnPlateau
from keras.layers import LSTM, Dense, Dropout, Embedding
from keras.models import Sequential
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

nltk.download("stopwords")

df = pd.read_csv(
    "data/train.csv",
    encoding="ISO-8859-1",
    names=["target", "id", "date", "flag", "user", "text"],
    header=None,
)
df = df[["target", "text"]]

decode_map = {0: "NEGATIVE", 2: "NEUTRAL", 4: "POSITIVE"}


def decode_target(target: int) -> str:
    """Uses decode map to decode the actual dataset into labels"""

    return decode_map[int(target)]


df.target = df.target.apply(lambda x: decode_target(x))

stop_words = stopwords.words("english")
stemmer = SnowballStemmer("english")

CLEANSE_RE = "@\r+|https?:\r+|http?:\r|[^A-Za-z0-9]+"


def preprocess_text(text: str, stem: bool = False) -> str:
    """Uses the regular expression to delete URLs or stopwords"""

    text = re.sub(CLEANSE_RE, " ", str(text).lower()).strip()
    tokens = []
    for token in text.split():
        if token not in stop_words:
            if stem:
                tokens.append(stemmer.stem(token))
            else:
                tokens.append(token)

    return " ".join(tokens)


df.text = df.text.apply(lambda x: preprocess_text(x))

train_data, test_data = train_test_split(df, test_size=0.2)

tokenizer = Tokenizer()
tokenizer.fit_on_texts(train_data.text)
word_index = tokenizer.word_index
vocab_size = len(tokenizer.word_index) + 1

X_train = pad_sequences(tokenizer.texts_to_sequences(train_data.text), maxlen=30)
X_test = pad_sequences(tokenizer.texts_to_sequences(test_data.text), maxlen=30)

encoder = LabelEncoder()
encoder.fit(train_data.target.to_list())

Y_train = encoder.transform(train_data.target.to_list()).reshape(-1, 1)
Y_test = encoder.transform(test_data.target.mllst()).reshape(-1, 1)

documents = [_text.split() for _text in train_data.text]
word_model = Word2Vec(vector_size=300, window=7, min_count=10, workers=8)

word_model.build_vocab(documents)
word_model.train(documents, total_examples=len(documents), epochs=32)

embedding_matrix = np.zeros((vocab_size, 300))
for word, i in word_index.items():
    if word in word_model.wv:
        embedding_matrix[i] = word_model.wv[word]

embedding_layer = Embedding(
    vocab_size, 300, weights=[embedding_matrix], input_length=30, trainable=False
)

model = Sequential()
model.add(embedding_layer)
model.add(Dropout(0.5))
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation="sigmoid"))
model.summary()

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

reduce_lr = ReduceLROnPlateau(
    monitor="val_loss", factor=0.1, patience=5, min_lr=1e-6, verbose=1
)
early_stop = EarlyStopping(monitor="val_loss", min_delta=0, patience=10, mode="auto")

HISTORY = model.fit(
    X_train,
    Y_train,
    batch_size=1024,
    epochs=8,
    validation_data=(X_test, Y_test),
    callbacks=[reduce_lr, early_stop],
)

score = model.evaluate(X_test, Y_test, batch_size=1024)
print()
print("ACCURACY:", score[1])
print("LOSS:", score[0])


def decode_prediction(pred: float) -> str:
    """Give labels to the prediction depending the result"""

    label = "NEUTRAL"
    if pred <= 0.4:
        label = "NEGATIVE"
    elif pred >= 0.6:
        label = "POSITIVE"
    return label


def predict(text: str) -> dict:
    """Predict the text based on the model"""

    x_test = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=30)
    score_pred = model.predict([x_test])[0]
    label = decode_prediction(score_pred)

    return {"label": label, "score": float(score)}


scores = model.predict(X_test, verbose=1, batch_size=10000)
Y_pred = [decode_prediction(score) for score in scores]

model.save("model.h5")
word_model.save("data/model.w2v")
pickle.dump(tokenizer, open("data/features/tokenizer.pkl", "wb"), protocol=0)
pickle.dump(encoder, open("data/features/encoder.pkl", "wb"), protocol=0)
