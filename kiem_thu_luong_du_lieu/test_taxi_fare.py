import pytest

from taxi_fare import TaxiFareCalculator

class TestTaxiFareCalculator:
    def setup_method(self):
        self.taxi_fare_calculator = TaxiFareCalculator()

    def test_tc1(self):
        with pytest.raises(ValueError):
            self.taxi_fare_calculator.calculate_fare(-1, 1)

    def test_tc2(self):
        with pytest.raises(ValueError):
            self.taxi_fare_calculator.calculate_fare(300, 1)

    def test_tc3(self):
        with pytest.raises(ValueError):
            self.taxi_fare_calculator.calculate_fare(10, 0)

    def test_tc4(self):
        with pytest.raises(ValueError):
            self.taxi_fare_calculator.calculate_fare(10, 6)

    def test_tc5(self):
        assert self.taxi_fare_calculator.calculate_fare(10, 1) == 210000

    def test_tc6(self):
        assert self.taxi_fare_calculator.calculate_fare(10, 2) == 252000

    def test_tc7(self):
        assert self.taxi_fare_calculator.calculate_fare(0.5, 1) == 30000

    def test_tc8(self):
        assert self.taxi_fare_calculator.calculate_fare(0.5, 2) == 36000

    def test_tc9(self):
        assert self.taxi_fare_calculator.calculate_fare(100, 1) == 1210000

    def test_tc10(self):
        assert self.taxi_fare_calculator.calculate_fare(100, 2) == 1452000
