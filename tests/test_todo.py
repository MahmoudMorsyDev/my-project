from lib.todo import Todo

def test_init():
    todo = Todo("groceries shopping")
    assert todo.task == "groceries shopping"

def test_mark_complete():
    todo = Todo("babysit")
    assert todo.complete == False
    todo.mark_complete()
    assert todo.complete == True