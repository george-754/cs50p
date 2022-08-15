# Testing the twttr app

from twttr import shorten

def test_assert():
    assert shorten("George") == "Grg"
    assert shorten("Jessie") == "Jss"
    assert shorten("MOLLY") == "MLLY"
    assert shorten("pearl") == "prl"
    assert shorten("opal") == "pl"
    assert shorten("Green smiles mean your program has passed a test!") == "Grn smls mn yr prgrm hs pssd  tst!"
    assert shorten("CS50") == "CS50"