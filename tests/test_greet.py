from lib.greet import *

def test_greet():
    greeting = greet('Mahmoud')
    assert greeting == "Hello, Mahmoud"