# Test plates.py app


from plates import is_valid


def test_numbers():
    assert is_valid("123456") == False
    assert is_valid("123C1") == False
    assert is_valid("abc12") == True
    assert is_valid("a12") == False
    assert is_valid("abc012") == False
    assert is_valid("012abc") == False
    assert is_valid("ABC124") == True
    assert is_valid("Unc23") == True
    assert is_valid("U0Me24") == False
    assert is_valid("AB12CD") == False
    assert is_valid("123Abc") == False


def test_length():
    assert is_valid("Ab") == True
    assert is_valid("1") == False
    assert is_valid("aBc") == True
    assert is_valid("oneOFMany") == False
    assert is_valid("TooMany1000") == False
    assert is_valid("SAM123") == True


def test_puctuation():
    assert is_valid("abc-12") == False
    assert is_valid("!#One") == False
    assert is_valid("--B--") == False
    assert is_valid("Hello!") == False
    assert is_valid("gr8$") == False


def test_correct():
    assert is_valid("FaSt") == True
    assert is_valid("ToFast") == True
    assert is_valid("GMa23") == True
    assert is_valid("LIVE4") == True
    assert is_valid("URGR8") == True
    assert is_valid("A1Sauce") == False