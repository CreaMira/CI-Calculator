import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(3, 2)

    def test_substract(self):
        assert 1 == calculator.subtract(3, 2)

    def test_mul(self):
        assert 6 == calculator.mul(3, 2)

    def test_div(self):
        assert 2 == calculator.div(4, 2)
