import pickle
import re
from math import pi

import pandas as pd
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
from matplotlib import pyplot as plt
from nltk.stem import SnowballStemmer

# Load model and CSV

model = load_model("../model.h5")
tokenizer = pickle.load(open("../data/features/tokenizer.pkl", "rb"))

df = pd.read_csv(
    "../data/tweets.csv",
    encoding="ISO-8859-1",
    names=["user", "text", "loc"],
    header=None,
)
df = df[["text"]]

## Text preprocessing

stemmer = SnowballStemmer("english")

cleanse_re = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"


def preprocess_text(text, stem=True):
    text = re.sub(cleanse_re, " ", str(text).lower()).strip()
    tokens = []
    for token in text.split():
        if stem:
            tokens.append(stemmer.stem(token))
        else:
            tokens.append(token)

    return " ".join(tokens)


df.text = df.text.apply(lambda x: preprocess_text(x))


# Give user friendly output of prediction


def decode_prediction(pred):
    label = "NEUTRAL"
    if pred <= 0.45:
        label = "NEGATIVE"
    elif pred >= 0.55:
        label = "POSITIVE"
    return label


def predict(text):
    X_text = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=30)
    score = model.predict([X_text])[0]
    label = decode_prediction(score)

    return {"message": text, "label": label, "score": float(score)}


# Create piechart

piechart = {"POSITIVE": 0, "NEUTRAL": 0, "NEGATIVE": 0}

for text in df.text.to_list():
    res = predict(text)
    piechart[res["label"]] += 1

fig = plt.figure(figsize=(10, 7))
plt.pie(piechart.values(), labels=piechart.keys())
plt.savefig("pie.png")
