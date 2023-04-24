from lib.excercise_two import *
import pytest

""" 
"""
def test_grammar_checker():
    result = grammar_checker("Allo my name is mvmkfmk vn ej nvjen nvjef fbeh.")
    assert result == True

