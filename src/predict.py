""" Predicition Module"""

import pickle
import re
import typing

import pandas as pd
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from matplotlib import pyplot as plt
from nltk.stem import SnowballStemmer

model = load_model("model.h5")

df = pd.read_csv(
    "data/tweets.csv",
    encoding="ISO-8859-1",
    names=["user", "text", "loc"],
    header=None,
)
df = df[["text"]]

stemmer = SnowballStemmer("english")

CLEANSE_RE = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"


def preprocess_text(text: str, stem: bool = True) -> str:
    """Remove URLs and stopwords"""

    text = re.sub(CLEANSE_RE, " ", str(text).lower()).strip()
    tokens = []
    for token in text.split():
        if stem:
            tokens.append(stemmer.stem(token))
        else:
            tokens.append(token)

    return " ".join(tokens)


df.text = df.text.apply(lambda x: preprocess_text(x))


def decode_prediction(pred: float) -> str:
    """Decode prediction number to label"""

    label = "NEUTRAL"
    if pred <= 0.45:
        label = "NEGATIVE"
    elif pred >= 0.55:
        label = "POSITIVE"
    return label


tokenizer = pickle.load(open("data/features/tokenizer.pkl", "rb"))


def predict(text: str) -> typing.Dict:
    """Predict the text with model"""

    x_text = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=30)
    score = model.predict([x_text])[0]
    label = decode_prediction(score)

    return {"message": text, "label": label, "score": float(score)}


piechart = {"POSITIVE": 0, "NEUTRAL": 0, "NEGATIVE": 0}

for tweet in df.text.to_list():
    res = predict(tweet)
    piechart[res["label"]] += 1

fig = plt.figure(figsize=(10, 7))
plt.pie(piechart.values(), labels=piechart.keys())
plt.savefig("pie.png")
