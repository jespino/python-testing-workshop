from pytest import mark
import operator

@mark.bench('operator.eq')
def test_eq():
    assert operator.eq(1, 1)
