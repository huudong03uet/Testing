import pytest

from taxi_fare import TaxiFareCalculator

class TestTaxiFareCalculator:
    def setup_method(self):
        self.taxi_fare_calculator = TaxiFareCalculator()
    
    # Kiem thu bien
    def test_tc1(self):
        assert self.taxi_fare_calculator.calculate_fare(100, 1) == 1210000
    
    def test_tc2(self):
        assert self.taxi_fare_calculator.calculate_fare(100, 2) == 1452000
    
    def test_tc3(self):
        assert self.taxi_fare_calculator.calculate_fare(100, 3) == 1694000
    
    def test_tc4(self):
        assert self.taxi_fare_calculator.calculate_fare(100, 4) == 1936000
    
    def test_tc5(self):
        assert self.taxi_fare_calculator.calculate_fare(100, 5) == 2178000
    
    def test_tc6(self):
        assert self.taxi_fare_calculator.calculate_fare(0, 3) == 42000
    
    def test_tc7(self):
        assert self.taxi_fare_calculator.calculate_fare(0.1, 3) == 42000
    
    def test_tc8(self):
        assert self.taxi_fare_calculator.calculate_fare(199.9, 3) == 3092600
    
    def test_tc9(self):
        assert self.taxi_fare_calculator.calculate_fare(200, 3) == 3094000

    # Kiem thu bang quyet dinh
    def test_tc10(self):
        with pytest.raises(ValueError):
            self.taxi_fare_calculator.calculate_fare(100, -1)
    def test_tc11(self):
        with pytest.raises(ValueError):
            self.taxi_fare_calculator.calculate_fare(-1, 1)

    def test_tc12(self):
        assert self.taxi_fare_calculator.calculate_fare(0, 1) == 30000

    def test_tc13(self):
        assert self.taxi_fare_calculator.calculate_fare(10, 1) == 210000

    def test_tc14(self):
        assert self.taxi_fare_calculator.calculate_fare(100, 1) == 1210000

    def test_tc15(self):
        with pytest.raises(ValueError):
            self.taxi_fare_calculator.calculate_fare(300, 1)

    def test_tc16(self):
        with pytest.raises(ValueError):
            self.taxi_fare_calculator.calculate_fare(100, 6)

    def test_tc17(self):
        with pytest.raises(ValueError):
            self.taxi_fare_calculator.calculate_fare(-1, 2)

    def test_tc18(self):
        assert self.taxi_fare_calculator.calculate_fare(0, 2) == 36000
        
    def test_tc19(self):
        assert self.taxi_fare_calculator.calculate_fare(10, 2) == 252000

    def test_tc20(self):
        assert self.taxi_fare_calculator.calculate_fare(100, 2) == 1452000

    def test_tc21(self):
        with pytest.raises(ValueError):
            self.taxi_fare_calculator.calculate_fare(300, 2)