# Test lines.py

from lines import count


def test_count():
    assert count("hello.py") == 7
    assert count("goodbye.py") == 0