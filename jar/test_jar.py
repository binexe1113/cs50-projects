import pytest
from jar import Jar

def test_negative_capacity():
    with pytest.raises(ValueError):
        Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(5)
    with pytest.raises(ValueError):
        jar.deposit(6)

def test_withdraw():
    jar = Jar(3)
    with pytest.raises(ValueError):
        jar.withdraw(4)
