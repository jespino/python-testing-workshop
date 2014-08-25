import calculator

calc = calculator.Calculator()

class TestClass:
    def test_add(self):
        assert calc.add(1, 1) == 2

    def test_sub(self):
        assert calc.sub(1, 1) == 0

    def test_bad(self):
        assert calc.sub(1, 1) == 8
