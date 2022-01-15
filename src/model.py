""" Machine Learning model to predict SA"""
import pickle
import re
import itertools
from collections import Counter

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
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

import matplotlib.pyplot as plt



nltk.download("stopwords")

DF = pd.read_csv(
    "data/train.csv",
    encoding="ISO-8859-1",
    names=["target", "id", "date", "flag", "user", "text"],
    header=None,
)
DF = DF[["target", "text"]]

DECODE_MAP = {0: "NEGATIVE", 2: "NEUTRAL", 4: "POSITIVE"}


def decode_target(target: int) -> str:
    """Uses decode map to decode the actual dataset into labels"""

    return DECODE_MAP[int(target)]


DF.target = DF.target.apply(lambda x: decode_target(x))

TARGET_CNT = Counter(DF.target)

plt.figure(figsize=(16, 8))
plt.bar(TARGET_CNT.keys(), TARGET_CNT.values())
plt.title("Dataset labels distribution")
plt.savefig("distribution.png")

STOP_WORDS = stopwords.words("english")
STEMMER = SnowballStemmer("english")

CLEANSE_RE = "@\r+|https?:\r+|http?:\r|[^A-Za-z0-9]+"


def preprocess_text(text: str, stem: bool = False) -> str:
    """Uses the regular expression to delete URLs or stopwords"""

    text = re.sub(CLEANSE_RE, " ", str(text).lower()).strip()
    tokens = []
    for token in text.split():
        if token not in STOP_WORDS:
            if stem:
                tokens.append(STEMMER.stem(token))
            else:
                tokens.append(token)

    return " ".join(tokens)


DF.text = DF.text.apply(lambda x: preprocess_text(x))

TRAIN_DATA, TEST_DATA = train_test_split(DF, test_size=0.2)

TOKENIZER = Tokenizer()
TOKENIZER.fit_on_texts(TRAIN_DATA.text)
WORD_INDEX = TOKENIZER.word_index
VOCAB_SIZE = len(TOKENIZER.word_index) + 1

X_TRAIN = pad_sequences(TOKENIZER.texts_to_sequences(TRAIN_DATA.text), maxlen=30)
X_TEST = pad_sequences(TOKENIZER.texts_to_sequences(TEST_DATA.text), maxlen=30)

ENCODER = LabelEncoder()
ENCODER.fit(TRAIN_DATA.target.to_list())

Y_TRAIN = ENCODER.transform(TRAIN_DATA.target.to_list()).reshape(-1, 1)
Y_TEST = ENCODER.transform(TEST_DATA.target.to_list()).reshape(-1, 1)

DOCUMENTS = [_text.split() for _text in TRAIN_DATA.text]
WORD_MODEL = Word2Vec(vector_size=300, window=7, min_count=10, workers=8)

WORD_MODEL.build_vocab(DOCUMENTS)
WORD_MODEL.train(DOCUMENTS, total_examples=len(DOCUMENTS), epochs=32)

EMBEDDING_MATRIX = np.zeros((VOCAB_SIZE, 300))
for word, index in WORD_INDEX.items():
    if word in WORD_MODEL.wv:
        EMBEDDING_MATRIX[index] = WORD_MODEL.wv[word]

EMBEDDING_LAYER = Embedding(
    VOCAB_SIZE, 300, weights=[EMBEDDING_MATRIX], input_length=30, trainable=False
)

MODEL = Sequential()
MODEL.add(EMBEDDING_LAYER)
MODEL.add(Dropout(0.5))
MODEL.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
MODEL.add(Dense(1, activation="sigmoid"))
MODEL.summary()

MODEL.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

REDUCE_LR = ReduceLROnPlateau(
    monitor="val_loss", factor=0.1, patience=5, min_lr=1e-6, verbose=1
)
EARLY_STOP = EarlyStopping(monitor="val_loss", min_delta=0, patience=10, mode="auto")

HISTORY = MODEL.fit(
    X_TRAIN,
    Y_TRAIN,
    batch_size=1024,
    epochs=8,
    validation_data=(X_TEST, Y_TEST),
    callbacks=[REDUCE_LR, EARLY_STOP],
)


ACC = HISTORY.history['accuracy']
VAL_ACC = HISTORY.history['val_accuracy']
LOSS = HISTORY.history['loss']
VAL_LOSS = HISTORY.history['val_loss']
EPOCHS = range(len(ACC))

plt.plot(EPOCHS, ACC, 'b', label='Training acc')
plt.plot(EPOCHS, VAL_ACC, 'r', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()

plt.savefig('training_acc.png')

plt.figure()

plt.plot(EPOCHS, LOSS, 'b', label='Training loss')
plt.plot(EPOCHS, VAL_LOSS, 'r', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()

plt.savefig('training_loss.png')

SCORE = MODEL.evaluate(X_TEST, Y_TEST, batch_size=1024)
print(SCORE)
print("ACCURACY:", SCORE[1])
print("LOSS:", SCORE[0])


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

    x_test = pad_sequences(TOKENIZER.texts_to_sequences([text]), maxlen=30)
    score_pred = MODEL.predict([x_test])[0]
    label = decode_prediction(score_pred)

    return {"label": label, "score": float(SCORE)}

Y_PRED_1D = []
Y_TEST_1D = list(TEST_DATA.target)

def plot_confusion_matrix(conf_matrix, classes,
                          title='Confusion matrix'):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """

    conf_matrix = conf_matrix.astype('float') / conf_matrix.sum(axis=1)[:, np.newaxis]

    plt.imshow(conf_matrix, interpolation='nearest')
    plt.title(title, fontsize=30)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=90, fontsize=22)
    plt.yticks(tick_marks, classes, fontsize=22)

    fmt = '.2f'
    thresh = conf_matrix.max() / 2.
    for i, j in itertools.product(range(conf_matrix.shape[0]), range(conf_matrix.shape[1])):
        plt.text(j, i, format(conf_matrix[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if conf_matrix[i, j] > thresh else "black")

    plt.ylabel('True label', fontsize=25)
    plt.xlabel('Predicted label', fontsize=25)

CNF_MATRIX = confusion_matrix(Y_TEST_1D, Y_PRED_1D)
plt.figure(figsize=(12, 12))
plot_confusion_matrix(CNF_MATRIX, classes=TRAIN_DATA.target.unique(), title="Confusion matrix")
plt.savefig('cnf_matrix.png')

SCORES = MODEL.predict(X_TEST, verbose=1, batch_size=8000)
Y_PRED_1D = [decode_prediction(score) for score in SCORES]

print(classification_report(Y_TEST_1D, Y_PRED_1D))
accuracy_score(Y_TEST_1D, Y_PRED_1D)

SCORES = MODEL.predict(X_TEST, verbose=1, batch_size=10000)
Y_PRED = [decode_prediction(score) for score in SCORES]

MODEL.save("model.h5")
WORD_MODEL.save("data/model.w2v")
pickle.dump(TOKENIZER, open("data/features/tokenizer.pkl", "wb"), protocol=0)
pickle.dump(ENCODER, open("data/features/encoder.pkl", "wb"), protocol=0)
