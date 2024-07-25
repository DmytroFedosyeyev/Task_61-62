import unittest
from Task import Fraction

class TestFraction(unittest.TestCase):
    def test_addition(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 + f2
        self.assertEqual(result.num, 5)
        self.assertEqual(result.divider, 6)

    def test_subtraction(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 - f2
        self.assertEqual(result.num, 1)
        self.assertEqual(result.divider, 6)

    def test_multiplication(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 * f2
        self.assertEqual(result.num, 1)
        self.assertEqual(result.divider, 6)

    def test_division(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 3)
        result = f1 / f2
        self.assertEqual(result.num, 3)
        self.assertEqual(result.divider, 2)

    def test_division_by_zero(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(0, 1)
        with self.assertRaises(ValueError):
            f1 / f2

    def test_equality(self):
        f1 = Fraction(1, 2)
        f2 = Fraction(1, 2)
        f3 = Fraction(2, 3)
        self.assertTrue(f1 == f2)
        self.assertFalse(f1 == f3)

    def test_str(self):
        f1 = Fraction(1, 2)
        self.assertEqual(str(f1), "1/2")

if __name__ == '__main__':
    unittest.main()
