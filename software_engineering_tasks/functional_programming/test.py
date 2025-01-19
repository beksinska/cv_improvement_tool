import unittest
from filtering_numbers import is_odd, double, square, apply_function_to_list

class TestFunctionalOperations(unittest.TestCase):
    def setUp(self):
        self.test_numbers = [1, 2, 3, 4, 5]
        
    def test_is_odd(self):
        #Test the is_odd function with various inputs
        self.assertTrue(is_odd(1))
        self.assertFalse(is_odd(2))
        self.assertTrue(is_odd(3))
        self.assertFalse(is_odd(0))
        self.assertTrue(is_odd(-1))
        
    def test_double(self):
        #Test the double function with various inputs
        self.assertEqual(double(2), 4)
        self.assertEqual(double(0), 0)
        self.assertEqual(double(-1), -2)
        
    def test_square(self):
        #Test the square function with various inputs
        self.assertEqual(square(2), 4)
        self.assertEqual(square(0), 0)
        self.assertEqual(square(-2), 4)
        
    def test_apply_function_to_list(self):
        # Test the higher-order function
        # Test with double function
        result_double = apply_function_to_list(double, self.test_numbers)
        self.assertEqual(result_double, [2, 4, 6, 8, 10])
        
        # Test with square function
        result_square = apply_function_to_list(square, self.test_numbers)
        self.assertEqual(result_square, [1, 4, 9, 16, 25])
        
        # Test with empty list
        self.assertEqual(apply_function_to_list(double, []), [])
        
    def test_full_workflow(self):
        # Test the complete workflow of filtering, doubling, and squaring
        odd_numbers = list(filter(is_odd, self.test_numbers))
        self.assertEqual(odd_numbers, [1, 3, 5])
        
        doubled_odds = apply_function_to_list(double, odd_numbers)
        self.assertEqual(doubled_odds, [2, 6, 10])
        
        squared_odds = apply_function_to_list(square, odd_numbers)
        sum_of_squares = sum(squared_odds)
        self.assertEqual(squared_odds, [1, 9, 25])
        self.assertEqual(sum_of_squares, 35)

if __name__ == '__main__':
    unittest.main()