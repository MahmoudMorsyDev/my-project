from lib.design_class import *

def test_user_todo():
    """
        Given a task title and a task description
        #add_task adds a new task to the dictionary of tasks
    """
    """ Given a task title
        #done_task changes the status of the task to done and that removes it from the dictionary
    """
    """
        #get_all_tasks return the list of undone tasks 
    """
    user_todo = UserTodo()
    user_todo.add_task("Cleaning Bathroom", "Clean the bathtub, the sink and the toilet")
    assert user_todo.get_all_todo_tasks() == ["Cleaning Bathroom: Clean the bathtub, the sink and the toilet"]
    user_todo.add_task("Cooking", "Cook some food")
    user_todo.done_task("Cooking")
    assert user_todo.get_all_todo_tasks() == ["Cleaning Bathroom: Clean the bathtub, the sink and the toilet"]
