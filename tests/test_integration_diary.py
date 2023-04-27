from lib.diary import Diary
from lib.diary_entry import DiaryEntry
"""
Given a title and content
A data entry can be added to a diary
"""
def test_add_entries_in_diary_and_view_all():
    diary = Diary()
    entry1 = DiaryEntry("hello", "today im feeling good")
    diary.add(entry1)
    assert diary.entry_list == [entry1]
    assert diary.all() == [entry1]

"""
Given multiple diary entries
We want to get the number of words within all entries
"""
def test_count_words():
    diary = Diary()
    entry2 = DiaryEntry("hi", "today im feeling bad")
    diary.add(entry2)
    assert diary.count_words() == 4
    entry3 = DiaryEntry("hola", "today im feeling beautiful")
    diary.add(entry3)
    assert diary.count_words() == 8

"""
Given a diary with multiple entries
we want to get the estimate time of reading all entries in the list of entries
"""
def test_reading_time():
    diary = Diary()
    entry2 = DiaryEntry("hello", "hi how are you")
    entry3 = DiaryEntry("hey", "hey how are you")
    diary.add(entry2)
    diary.add(entry3)
    assert diary.reading_time(2) == 4

def test_best_entry_for_reading_time():
    diary = Diary()
    entry = DiaryEntry("Hello", "lko kkl hmk uui yyh nbh nbh nbh")#8
    entry_a = DiaryEntry("Good Morning", "asdasd asdasd asdasdasd asdasd")#4    
    entry_aa = DiaryEntry("Good afternoon", "qwe qwe ert rty rty rtty cvb njy fkhty kjhy nby nby")#12
    diary.add(entry)
    diary.add(entry_a)
    diary.add(entry_aa)
    assert diary.find_best_entry_for_reading_time(2, 6) == entry_aa
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_a
    assert diary.find_best_entry_for_reading_time(1, 3) == "error"
