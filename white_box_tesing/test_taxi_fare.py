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
            self.taxi_fare_calculator.calculate_fare(1, -1)
    
    def test_tc3(self):
        assert self.taxi_fare_calculator.calculate_fare(10, 2) == 252000
    
    def test_tc4(self):
        assert self.taxi_fare_calculator.calculate_fare(40, 2) == 732000
    
    def test_tc5(self):
        assert self.taxi_fare_calculator.calculate_fare(0.5, 1) == 30000