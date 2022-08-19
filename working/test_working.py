# Test the working.py program

from working import convert
import pytest


def test_single():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 PM to 9 AM") == "12:00 to 09:00"
    assert convert("12 AM to 8 AM") == "00:00 to 08:00"
    with pytest.raises(ValueError):
        assert convert("13 AM to 5 PM")
    with pytest.raises(ValueError):
        assert convert("1Pm to 2 AM")


def test_long():
    assert convert("12:30 AM to 5:44 PM") == "00:30 to 17:44"
    assert convert("4:15 PM to 12:30 PM") == "16:15 to 12:30"
    assert convert("6:00 PM to 1:30 AM") == "18:00 to 01:30"
    with pytest.raises(ValueError):
        assert convert("13:24 PM to 4:30 AM")
    with pytest.raises(ValueError):
        assert convert("cat")
    with pytest.raises(ValueError):
        assert convert("4:30 PM to 1:00")
    with pytest.raises(ValueError):
        assert convert("4:67 Pm to 14:78 AM")


def test_mix():
    assert convert("1 PM to 12:30 AM") == "13:00 to 00:30"
    assert convert("7 AM to 3:57 PM") == "07:00 to 15:57"
    assert convert("5:45 AM to 1 PM") == "05:45 to 13:00"
    with pytest.raises(ValueError):
        assert convert("5:30PM to 7 AM")
    with pytest.raises(ValueError):
        assert convert("5 PM - 3:21 AM")
    with pytest.raises(ValueError):
        assert convert("1:30 PM - 17:45")
