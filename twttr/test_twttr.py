import pytest
from twttr import shorten
def test_short():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"
    assert shorten("hi1!")  ==  "h1!"

