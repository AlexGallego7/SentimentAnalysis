""" Predicition Module"""

import pickle
import re

import pandas as pd
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from matplotlib import pyplot as plt
from nltk.stem import SnowballStemmer

#MODEL = load_model("saved_model.pb")

DF = pd.read_csv(
    "data/tweets.csv",
    encoding="ISO-8859-1",
    names=["user", "text", "loc"],
    header=None,
)
DF = DF[["text"]]

STEMMER = SnowballStemmer("english")

CLEANSE_RE = "@\r+|https?:\r+|http?:\r|[^A-Za-z0-9]+"


def preprocess_text(text: str, stem: bool = True) -> str:
    """Remove URLs and stopwords"""

    text = re.sub(CLEANSE_RE, " ", str(text).lower()).strip()
    tokens = []
    for token in text.split():
        if stem:
            tokens.append(STEMMER.stem(token))
        else:
            tokens.append(token)

    return " ".join(tokens)


DF.text = DF.text.apply(lambda x: preprocess_text(x))


def decode_prediction(pred: float) -> str:
    """Decode prediction number to label"""

    label = "NEUTRAL"
    if pred <= 0.45:
        label = "NEGATIVE"
    elif pred >= 0.55:
        label = "POSITIVE"
    return label


TOKENIZER = pickle.load(open("data/features/tokenizer.pkl", "rb"))
MODEL = pickle.load(open("Sentiment-LR.pickle", "rb"))


def predict(text: str) -> dict:
    """Predict the text with model"""

    x_text = pad_sequences(TOKENIZER.texts_to_sequences([preprocess_text(text)]), maxlen=30)
    score = MODEL.predict([text])
    label = decode_prediction(score)

    return {"message": text, "label": label, "score": float(score)}


PIECHART = {"POSITIVE": 0, "NEUTRAL": 0, "NEGATIVE": 0}

print(predict("HELLO"))

FIG = plt.figure(figsize=(10, 7))
plt.pie(PIECHART.values(), labels=PIECHART.keys())
plt.savefig("pie.png")
