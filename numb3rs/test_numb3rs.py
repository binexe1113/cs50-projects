import pytest
from numb3rs import validate

def test_val():
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("255.255.255.700") == False

