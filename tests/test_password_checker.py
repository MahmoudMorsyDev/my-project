from lib.password_checker import *
import pytest

def test_password_checker():
    passwordChecker = PasswordChecker()
    with pytest.raises(Exception) as e:
        passwordChecker.check("kfoor")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."
    result = passwordChecker.check("kfoorfkjnnj")
    assert result == True