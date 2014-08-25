import pytest

def func(x):
    return x + 1

@pytest.mark.bad
def test_bad():
    assert func(3) == 5

@pytest.mark.good
def test_good():
    assert func(4) == 5
