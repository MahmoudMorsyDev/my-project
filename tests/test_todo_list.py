from lib.todo_list import TodoList

def test_init():
    todo_list = TodoList()
    assert todo_list.todos_list == []