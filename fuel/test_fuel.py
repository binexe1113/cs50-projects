import pytest

from fuel import convert, gauge

def test_str():
    with pytest.raises(ValueError):
        convert("bc")
        convert("b/c")
        convert("b/30")

def test_a():
    with pytest.raises(ValueError):
        convert("5/-3")

def test_b():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_c ():
    assert gauge(convert("0/100")) == "E"

def test_d ():
    assert gauge(convert("100/100")) == "F"
def test_e():
    assert gauge(1) == "E"
def test_f():
    assert gauge(99)=="F"
