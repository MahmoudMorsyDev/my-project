from lib.task_tracker import *


"""
Given a text containing the string "#TODO",
it returns True  
"""
def test_includes_todo():
    result = does_include_todo("#TODO lkajsdlkajsdk")
    assert result == True
"""
Given a text not containing the string "#TODO",
it returns False  
"""
def test_doesnt_include_todo():
    result = does_include_todo("#TO asjdhasjkdhasd")
    assert result == False