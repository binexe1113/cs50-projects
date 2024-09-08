import pytest

from bank import value

def test_value():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("hey") == 20
    assert value("sup") == 100
