from lib.multiclass_diary import Diary

def test_diary_init():
    diary = Diary()
    assert diary.diary_entries_list == []
    assert diary.todo_list == []