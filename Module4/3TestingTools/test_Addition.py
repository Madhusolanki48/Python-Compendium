import Addition
import pytest

def test_add():
    assert True
    assert Addition.add(4,5) == 9

def test_sub():
    assert Addition.sub(4,5) == -1

    # to run in terminal ---  python -m pytest .\Module4\3TestingTools\TestAddition.py
    # assert Addition.sub(4,5) == -2 ---this will show one test case pass only

    # or 
def test_sub():
    pass