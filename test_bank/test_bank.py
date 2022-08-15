# Test the bank app with 3 functions

from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("Hello") == 0
    assert value("HeLlO") == 0


def test_h():
    assert value("happy") == 20
    assert value("Have a nice day") == 20
    assert value("How are you doing") == 20
    assert value("hey 007") == 20
    assert value("hel") == 20
    assert value("H") == 20


def test_all():
    assert value("What's up?") == 100
    assert value("Good morning. Hello") == 100
    assert value("good afternoon. Have a nice day!") == 100
    assert value("Nice to see you again. How have you been") == 100
    assert value("24 come on up") == 100