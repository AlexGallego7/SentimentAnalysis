import sys

sys.path.insert(1, '/home/alex/Desktop/SentimentAnalysis/src')

from predict import predict


def test_is_positive():
    assert (predict("What a nice day")["label"]) == "POSITIVE"
    assert (predict("I really enjoyed today's program")["label"]) == "POSITIVE"
    assert (predict("I got the job!")["label"]) == "POSITIVE"