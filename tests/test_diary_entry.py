from lib.diary_entry import DiaryEntry
"""
Given an entry
Give the amount of words in the contents
"""
def test_count_words():
    entry = DiaryEntry("hi", "nfnw ej nf jg n")
    assert entry.count_words() == 5

"""
Given an entry and a reading rate (wpm)
Return the reading time in minutes
"""
def test_reading_time():
    entry = DiaryEntry("hello", "nfnw ej nf jg n ncja cnbaj cjan")
    assert entry.reading_time(2) == 4

"""
Given an entry, words that can be read per minute,
and the time in minutes defined by the user.
Return a string representing a chunk of the contents that the user could read in the given
number of minutes
"""    
def test_reading_chunk():
    entry = DiaryEntry("Entry", "This is a new Diary Entry bla two")
    assert entry.reading_chunk(3, 1) == "This is a"
    assert entry.reading_chunk(3, 1) == "new Diary Entry"
    assert entry.reading_chunk(3, 1) == "bla two"
    assert entry.reading_chunk(3, 1) == "This is a"
