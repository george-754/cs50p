# Test the um.py counter program

from um import count



def test_fullwords():
    assert count("circumstantial") == 0
    assert count("enumerabilities") == 0
    assert count("humidifications") == 0
    assert count("overdocumenting") == 0
    assert count("disequilibriums") == 0


def test_sentences():
    assert count("Um, how are you doing") == 1
    assert count("Yum, how um, yummy are these cookies") == 1
    assert count("UM, what was I trying to um, say thats right argumentatively") == 2
    assert count("Undoubtedly um, unpredictable um, yeah") == 2
    assert count("What in the Um, world") == 1


def test_mix():
    assert count("Um, so uncontrollably humorlessness") == 1
    assert count("Humiliate um, that's not a good \"um\" thing to do") == 2
    assert count("So UM, what is beryllium") == 1
    assert count("Who is um, the recumbant") == 1
    assert count("..Um?... I don't know what um, I was thinking") == 2
    assert count("uM........?????") == 1