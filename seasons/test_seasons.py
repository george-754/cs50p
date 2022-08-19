# Test seasons.py


from seasons import convert
import pytest



def test_dates():
    assert convert("1999-07-07") == "Twelve million, one hundred fifty-nine thousand, three hundred sixty minutes"
    with pytest.raises(SystemExit):
        assert convert("2010-1-09")
    with pytest.raises(SystemExit):
        assert convert("99-06-23")
    with pytest.raises(SystemExit):
        assert convert("1998/03/24")
    with pytest.raises(SystemExit):
        assert convert("August 23, 1989")
    with pytest.raises(SystemExit):
        assert convert("10-23-2010")
    with pytest.raises(SystemExit):
        assert convert("2001-13-28")
    with pytest.raises(SystemExit):
        assert convert("2009-11-36")
    with pytest.raises(SystemExit):
        assert convert("dog")