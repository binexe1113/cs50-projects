import pytest
from um import count
def test1():
    assert count("um hello um") == 2
    assert count("yuumi") == 0
    assert count("um... you are um, one, um, person, um!") == 4
    assert count("UM who are you?") == 1
