from lib.present import *
import pytest
def test_present_wrap():
    present = Present()
    present.wrap("akjshd")
    with pytest.raises(Exception) as e:
        present.wrap('kajdskasjd')
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_present_unwrap_None():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."
    
def test_present_unwrap_value():
    present = Present()
    present.wrap("kgsokgoksd")
    result = present.unwrap()
    assert result == "kgsokgoksd"
