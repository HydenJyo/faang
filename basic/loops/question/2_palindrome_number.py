# Write a program to a given number is palindrome or not.

def palindrome(n):
    a = 0
    
    return a

import unittest

class Test(unittest.TestCase):
    def test_two_num_sum1(self):
        actual = palindrome(159357)
        expected = "Not Palindrome"
        self.assertEqual(actual, expected)
    def test_two_num_sum2(self):
        actual = palindrome(63636)
        expected = "Palindrome"
        self.assertEqual(actual, expected)
    def test_two_num_sum3(self):
        actual = palindrome(45)
        expected = "Not Palindrome"
        self.assertEqual(actual, expected)
    def test_two_num_sum4(self):
        actual = palindrome(7)
        expected = "Palindrome"
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)
