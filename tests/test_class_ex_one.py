from lib.class_ex_one import *

def test_diary_entry():
    diary_entry = DiaryEntry("My Diary", "this is my diary and that is my own book")
    assert diary_entry.format() == "My Diary: this is my diary and that is my own book"
    assert diary_entry.count_words() == 12
    assert diary_entry.reading_time(1) == 10
    assert diary_entry.reading_chunk(1, 3) == "this is my"
    assert diary_entry.reading_chunk(1,3) == "diary and that"
