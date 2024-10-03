import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # Test for the addition method
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)  # Positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)  # Positive and negative number
        self.assertEqual(self.calc.add(0, 0), 0)  # Both zero
        self.assertEqual(self.calc.add(-5, -5), -10)  # Negative numbers

    # Test for the subtraction method
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Positive numbers
        self.assertEqual(self.calc.subtract(-1, 1), -2)  # Positive and negative number
        self.assertEqual(self.calc.subtract(0, 0), 0)  # Both zero
        self.assertEqual(self.calc.subtract(-5, -5), 0)  # Negative numbers

    # Test for the multiplication method
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)  # Positive numbers
        self.assertEqual(self.calc.multiply(-1, 1), -1)  # Positive and negative number
        self.assertEqual(self.calc.multiply(0, 5), 0)  # Multiplying by zero
        self.assertEqual(self.calc.multiply(-5, -5), 25)  # Negative numbers

    # Test for the division method
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)  # Positive numbers
        self.assertEqual(self.calc.divide(-10, 2), -5)  # Positive and negative number
        self.assertEqual(self.calc.divide(0, 5), 0)  # Zero divided by a number
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero
        self.assertEqual(self.calc.divide(-10, -2), 5)  # Negative numbers

# Run the tests
if __name__ == "__main__":
    unittest.main()

