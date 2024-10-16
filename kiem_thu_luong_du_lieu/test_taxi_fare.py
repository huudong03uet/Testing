import pytest
from taxi_fare import TaxiFareCalculator

class TestTaxiFareCalculator:
    def setup_method(self):
        self.taxi_fare_calculator = TaxiFareCalculator()

    def test_tc1(self):
        assert self.taxi_fare_calculator.calculate_fare(10, 2) == 252000

    def test_tc2(self):
        with pytest.raises(ValueError):
            self.taxi_fare_calculator.calculate_fare(-1, 1)

    def test_tc3(self):
        assert self.taxi_fare_calculator.calculate_fare(10, 2) == 252000

    def test_tc4(self):
        assert self.taxi_fare_calculator.calculate_fare(0.5, 1) == 30000

    def test_tc5(self):
        assert self.taxi_fare_calculator.calculate_fare(10, 2) == 252000

    def test_tc6(self):
        assert self.taxi_fare_calculator.calculate_fare(40, 1) == 610000

    def test_tc7(self):
        assert self.taxi_fare_calculator.calculate_fare(40, 1) == 610000

    def test_tc8(self):
        assert self.taxi_fare_calculator.calculate_fare(10, 2) == 252000

    def test_tc9(self):
        with pytest.raises(ValueError):
            self.taxi_fare_calculator.calculate_fare(1, -1)

    def test_tc10(self):
        assert self.taxi_fare_calculator.calculate_fare(10, 2) == 252000

    def test_tc11(self):
        assert self.taxi_fare_calculator.calculate_fare(10, 2) == 252000

    def test_tc12(self):
        assert self.taxi_fare_calculator.calculate_fare(40, 1) == 610000

    def test_tc13(self):
        assert self.taxi_fare_calculator.calculate_fare(10, 2) == 252000

    def test_tc14(self):
        assert self.taxi_fare_calculator.calculate_fare(40, 1) == 610000

    def test_tc15(self):
        assert self.taxi_fare_calculator.calculate_fare(10, 2) == 252000

    def test_tc16(self):
        assert self.taxi_fare_calculator.calculate_fare(0.5, 1) == 30000

    def test_tc17(self):
        assert self.taxi_fare_calculator.calculate_fare(0.5, 2) == 36000

    def test_tc18(self):
        assert self.taxi_fare_calculator.calculate_fare(40, 1) == 610000

    def test_tc19(self):
        assert self.taxi_fare_calculator.calculate_fare(40, 1) == 610000

    def test_tc20(self):
        assert self.taxi_fare_calculator.calculate_fare(40, 2) == 732000

    def test_tc21(self):
        assert self.taxi_fare_calculator.calculate_fare(40, 1) == 610000

    def test_tc22(self):
        assert self.taxi_fare_calculator.calculate_fare(40, 2) == 732000

    def test_tc23(self):
        assert self.taxi_fare_calculator.calculate_fare(10, 1) == 210000

    def test_tc24(self):
        assert self.taxi_fare_calculator.calculate_fare(10, 2) == 252000
