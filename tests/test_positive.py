"""Test Positive Module"""

from predict import predict

def test_is_positive():
    """Test positive prediction"""

    assert (predict("What a nice day")["label"]) == "POSITIVE"
    assert (predict("I really enjoyed today's program")["label"]) == "POSITIVE"
    assert (predict("I got the job!")["label"]) == "POSITIVE"
