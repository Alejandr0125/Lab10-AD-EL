import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(3, 6), 9)
        pass

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(3, 2),1)
        self.assertEqual(sub(5, 3), 2)
        self.assertAlmostEqual(sub(6.7, 2.7), 4.0)
        pass
    ##########################

    # Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 10), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(self.calc.divide(6, 2), 3)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertRaises(ZeroDivisionError, self.calc.divide, 5, 0)

    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)
        pass

    def test_logarithm(self): # 3 assertions
        self.assertEqual(math.log(100,10),2)
        self.assertEqual(math.log(8, 2), 3)
        self.assertEqual(math.log(1, 10), 0)
        pass

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            log(100, 0)
        pass
    ##########################
    
    # Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            self.calc.logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(self.calc.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(self.calc.hypotenuse(5, 12), 13)
        self.assertAlmostEqual(self.calc.hypotenuse(8, 15), 17)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        pass
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()