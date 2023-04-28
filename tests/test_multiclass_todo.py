from lib.multiclass_todo import Todo

def test_todo_init():
    todo = Todo('banana')
    assert todo.task == "banana"