import unittest

from calculator import Calculator

class CalculatorTest(unittest.TestCase):
    def test_add(self):
        sut = Calculator()
        self.assertEqual(3, sut.add(1,2))

if __name__ == '__main__':
    unittest.main()