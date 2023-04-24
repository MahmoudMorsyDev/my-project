from lib.string_builder import *

def test_string_builder():
    string = StringBuilder()
    string.add("hello")
    size = string.size()
    result = string.output()
    assert size == 5
    assert result == "hello" 