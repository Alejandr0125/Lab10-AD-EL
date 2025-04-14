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
        self.assertEqual(subtract(3, 2),1)
        self.assertEqual(subtract(5, 3), 2)
        self.assertAlmostEqual(subtract(6.7, 2.7), 4.0)
        pass
    ##########################

    # Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-1, 5), -5)
        self.assertEqual(mul(0, 10), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(6, 2), 3)
        self.assertEqual(div(-9, 3), -3)
        self.assertRaises(ZeroDivisionError, div, 5, 0)

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
            logarithm(100, 0)
        pass
    ##########################
    
    # Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(8, 15), 17)

    class TestCalculator(unittest.TestCase):
        ######### Partner 2
        def test_add(self):  # 3 assertions
            self.assertEqual(add(2, 3), 5)
            self.assertEqual(add(-4, 9), 5)
            self.assertEqual(add(0, 0), 0)
            self.assertEqual(add(-2, -3), -5)

        def test_subtract(self):  # 3 assertions
            self.assertEqual(subtract(10, 4), 6)
            self.assertEqual(subtract(-2, -3), 1)
            self.assertEqual(subtract(0, 5), -5)
            self.assertEqual(subtract(5, 0), 5)

        ######## Partner 1
        def test_multiply(self):  # 3 assertions
            self.assertEqual(mul(5, 0), 0)
            self.assertEqual(mul(5, 1), 5)
            self.assertEqual(mul(-1, 5), -5)

        def test_divide(self):  # 3 assertions
            self.assertEqual(div(1, 5), 5)
            self.assertEqual(div(5, 5), 1)
            self.assertEqual(div(-5, 5), -1)

        ######## Partner 2
        def test_divide_by_zero(self):  # 1 assertion
            try:
                div(0, 5)
                self.fail("expected ZeroDivisionError not raised")
            except ZeroDivisionError:
                pass

        def test_logarithm(self):  # 3 assertions
            self.assertEqual(logarithm(10, 100), 2)
            self.assertEqual(round(logarithm(2, 8), 2), 3.00)
            self.assertEqual(round(logarithm(5, 25), 2), 2.00)

        def test_log_invalid_base(self):  # 1 assertion
            try:
                logarithm(1, 10)
                self.fail("expected ValueError not raised")
            except ValueError:
                pass

        ######## Partner 1
        def test_log_invalid_argument(self):  # 1 assertion
            with self.assertRaises(ValueError):
                logarithm(0, 5)

        def test_hypotenuse(self):  # 3 assertions
            self.assertEqual(hypotenuse(3, 4), 5)
            self.assertEqual(hypotenuse(-3, -4), 5)
            self.assertEqual(hypotenuse(0, 0), 0)

        def test_sqrt(self):  # 3 assertions
            with self.assertRaises(ValueError):
                square_root(-5)



# Do not touch this
if __name__ == "__main__":
    unittest.main()