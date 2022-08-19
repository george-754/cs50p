# Test jar.py.  Test the class functionality

from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert str(jar.capacity) == '12'



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(6)
    assert str(jar.size) == '6'
    jar.deposit(6)
    assert str(jar.size) == '12'
    with pytest.raises(ValueError):
        jar.deposit(4)
    


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    assert str(jar.size) == '10'
    jar.withdraw(5)
    assert str(jar.size) == '5'
    jar.withdraw(4)
    assert str(jar.size) == '1'
    with pytest.raises(ValueError):
        jar.withdraw(3)
