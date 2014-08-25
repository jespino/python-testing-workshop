import pytest

@pytest.mark.randomize(i1=int, i2=int, ncalls=10)
def test_generate_ints(i1, i2):
    assert i1 > i2
