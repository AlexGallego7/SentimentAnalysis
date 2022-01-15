"""Test Positive Module"""

import sys

from predict import predict

sys.path.insert(1, "/home/alex/Desktop/SentimentAnalysis/src")


def test_is_positive():
    assert (predict("What a nice day")["label"]) == "POSITIVE"
    assert (predict("I really enjoyed today's program")["label"]) == "POSITIVE"
    assert (predict("I got the job!")["label"]) == "POSITIVE"
