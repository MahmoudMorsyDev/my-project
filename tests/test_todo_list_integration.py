from lib.todo_list import TodoList
from lib.todo import Todo

def test_add_todo():
    todo_list = TodoList()
    todo1 = Todo("Kitchen")
    todo_list.add(todo1)
    assert todo_list.todos_list == [todo1]

def test_incomplete():
    todo_list = TodoList()
    todo1 = Todo("Kitchen")
    todo2 = Todo("bathroom")
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert todo_list.incomplete() == [todo1, todo2]
    todo1.mark_complete()
    assert todo_list.incomplete() == [todo2]

def test_complete():
    todo_list = TodoList()
    todo1 = Todo("living room")
    todo2 = Todo("cleaning")
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert todo_list.complete() == []
    todo1.mark_complete()
    assert todo_list.complete() == [todo1]

def test_give_up():
    todo_list = TodoList()
    todo1 = Todo("living room")
    todo2 = Todo("cleaning")
    todo_list.add(todo1)
    todo_list.add(todo2)
    assert todo_list.complete() == []
    todo_list.give_up()
    assert todo_list.incomplete() == []