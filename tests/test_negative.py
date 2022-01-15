""" Test Negative Module """

from predict import predict

def test_is_negative():
    """ Test negative prediction"""

    assert (predict("So boooring")["label"]) == "NEGATIVE"
    assert (predict("Had the worst day ever")["label"]) == "NEGATIVE"
    assert (
        predict("I really dont like what this program is doing")["label"]
    ) == "NEGATIVE"
