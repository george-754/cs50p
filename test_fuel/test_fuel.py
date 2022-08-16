# Test the fuel.py app

from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("4/4") == 100
    with pytest.raises(ZeroDivisionError):
        assert convert("4/0")

    with pytest.raises(ValueError):
        assert convert("5/4")


def test_gauge():
    assert gauge(10) == "10%"
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
