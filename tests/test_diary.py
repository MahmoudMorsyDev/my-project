from lib.diary import *

def test_make_snippet():
    result = make_snippet("Hello my name is Mahmoud, I am from Egypt")
    assert result == "Hello..."

def test_count_words():
    result = count_words("Bonjour je m'appelle Do")
    assert result == 4