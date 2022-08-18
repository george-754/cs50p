from numb3rs import validate


def test_numbers():
    assert validate("1.2.3.4") == True
    assert validate("124.156.178.199") == True
    assert validate("210.211.224.254") == True
    assert validate("192.0.1.256") == False
    assert validate("0.0.0.0") == True
    assert validate("256.278.123.456") == False
    assert validate("187.234.12.1.23") == False
    assert validate("197.65") == False
    assert validate("196.5.101") == False
    assert validate("196") == False


def test_alpha():
    assert validate("a.b.c.d") == False
    assert validate("23.45.67.c") == False
    assert validate("cs50") == False
    assert validate("c. 45. 67. 5") == False
    assert validate("34.t.67.89") == False