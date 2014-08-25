import pytest
import os

def func(x):
    return x + 1

@pytest.mark.bad
def test_bad():
    assert func(3) == 5

@pytest.mark.good
def test_good():
    assert func(4) == 5

@pytest.mark.cwd
def test_cwd_1(mock):
    mock.patch("os.getcwd")
    os.getcwd.return_value = "test"
    assert "test" == os.getcwd()

@pytest.mark.cwd
def test_cwd_2():
    assert "test" == os.getcwd()

@pytest.fixture
def mifixture():
    return 4

def test_with_fixture(mifixture):
    assert mifixture != 4
