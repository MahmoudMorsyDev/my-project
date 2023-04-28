from lib.multiclass_diary import Diary
from lib.multiclass_diary_entry import DiaryEntry
from lib.multiclass_todo import Todo

def test_add_todo():
    diary = Diary()
    todo = Todo("Do the Dishes")
    diary.add_todo(todo)
    assert diary.todo_list == [todo]

def test_add_diary_entry():
    diary = Diary()
    diary_entry = DiaryEntry("My first diary entry")
    diary.add_diary_entry(diary_entry)
    assert diary.diary_entries_list == [diary_entry]

def test_get_all_entries():
    diary = Diary()
    diary_entry_one = DiaryEntry("My First")
    diary_entry_two = DiaryEntry("My Second")
    diary_entry_three = DiaryEntry("My Third")
    diary.add_diary_entry(diary_entry_one)
    diary.add_diary_entry(diary_entry_two)
    diary.add_diary_entry(diary_entry_three)
    assert diary.get_all_entries() ==  [diary_entry_one, diary_entry_two, diary_entry_three]

def test_get_all_todos():
    diary = Diary()
    todo_one = Todo("My First")
    todo_two = Todo("My Second")
    todo_three = Todo("My Third")
    diary.add_todo(todo_one)
    diary.add_todo(todo_two)
    diary.add_todo(todo_three)
    assert diary.get_all_todos() ==  [todo_one, todo_two, todo_three]


def test_get_time_based_entries():
    diary = Diary()
    diary_entry_one = DiaryEntry("My First Diary for today if today is a good day")
    diary_entry_two = DiaryEntry("My Second Diary")
    diary_entry_three = DiaryEntry("it was the best of times it was the worst of times")
    diary_entry_four = DiaryEntry("ed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae t perspiciatis unde omnis iste natus error sit voluptatemt perspiciatis unde omnis iste natus error sit voluptatemab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.")
    diary_entry_five = DiaryEntry("vel illum t perspiciatis unde omnis iste natus error sit voluptatemt perspiciatis unde omnis iste natus error sit voluptatemt perspiciatis unde omnis iste natus error sit voluptatem qui dolorem eum fugiat quo voluptas nulla pariatur?")
    diary_entry_six = DiaryEntry("But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you a complete account of the system, and expound the actual teachings of the greatt perspiciatis unde omnis iste natus error sit voluptatemt perspiciatis unde omnis iste natus error sit voluptatemt perspiciatis unde omnis iste natus error sit voluptatem explorer of the truth, the master-builder of human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do")
    diary.add_diary_entry(diary_entry_one)
    diary.add_diary_entry(diary_entry_two)
    diary.add_diary_entry(diary_entry_three)
    diary.add_diary_entry(diary_entry_four)
    diary.add_diary_entry(diary_entry_five)
    diary.add_diary_entry(diary_entry_six)
    assert diary.get_time_based_entries(4, 5) == [diary_entry_one, diary_entry_two, diary_entry_three]

