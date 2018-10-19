from unittest import TestCase
from calculator.logic import Calculator
import pytest

class CalculatorTests(TestCase):
    def test_mul_with_two_positive_numbers(self):
        c = Calculator()
        assert c.mul(5, 10) == 50
    
    def test_mul_with_two_negative_numbers(self):
        c = Calculator()
        assert c.mul(-5, -10) == 50
    
    def test_mul_with_one_negative_one_positive_number(self):
        c = Calculator()
        assert c.mul(-5, 10) == -50

    def test_calculator_throws_e_when_out_of_bounds_low(self):
        with pytest.raises(ValueError):
            c = Calculator()
            c.mul(-1001,100)

    def test_div_with_two_positive_numbers(self):
        c = Calculator()
        assert c.div(50, 10) == 5

    def test_div_with_two_negative_numbers(self):
        c = Calculator()
        assert c.div(-50, -10) == 5
    
    def test_div_with_one_negative_one_positive_number(self):
        c = Calculator()
        assert c.div(-50, 10) == -5

    def test_div_throws_e_when_dividing_by_zero(self):
        with pytest.raises(ValueError):
            c = Calculator()
            c.div(50, 0)
