from lib.debug_exercises import *

def test_say_hello():
    result = say_hello("kay")
    assert result == "hello kay"

def test_encode():
    result = encode("theswiftfoxjumpedoverthelazydog", "secretkey")
    assert result == "EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL"

def test_decode():
    result = decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
    assert result == "theswiftfoxjumpedoverthelazydog"

def test_get_most_common_letter():
    result = get_most_common_letter("the roof, the roof, the roof is on fire!")
    assert result == "o"