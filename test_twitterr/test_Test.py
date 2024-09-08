import pytest
from twttr.test_twttr import shorten
def test_short():
    assert shorten("hello") == "hll"
    assert shorten("HELLO") == "HLL"

