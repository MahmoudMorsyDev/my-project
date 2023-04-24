from lib.excercise_one import *
import pytest

""" Given a 10 words text and a rate of 10 words per minute
    It returns a string saying it requires 1.0 minutes to read.
"""
def test_estimate_reading_time():
    result = estimate_reading_time("Allo my name is mvmkfmk vn ej nvjen nvjef fbeh", 10)
    assert result == 'Your estimate time is 1.0 minutes'

""" Given a number for the text and a rate of 10 words per minute
    It returns an error saying that the text inputted needs to be a string.
"""
def test_estimate_reading_time_wrong_text():
    with pytest.raises(Exception) as e:
        estimate_reading_time(78, 10)
    error_message = str(e.value)
    assert error_message == "Text given should be a string!"