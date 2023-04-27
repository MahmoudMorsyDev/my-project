from lib.diary import Diary

"""
Given a diary with no entry
Get a word count of 0
"""
def test_count_words_0():
    diary = Diary()
    assert diary.count_words() == 0

"""

"""