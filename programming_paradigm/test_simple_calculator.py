import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(2,3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(3,3), 6)
        self.assertNotEqual(self.calc.add(7,3), 20)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(8,3), 5)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertNotEqual(self.calc.subtract(3, -2), 1)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 12), 36)
        self.assertEqual(self.calc.multiply(6, 0), 0)
        self.assertNotEqual(self.calc.multiply(10, 3), 80)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(3,1), 3)
        self.assertEqual(self.calc.divide(4, 0), None)
        self.assertNotEqual(self.calc.divide(2, -2), 1)
        