import unittest
import palindrome


class PalindromeTest(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(palindrome.is_palindrome("redivider"))
        self.assertTrue(palindrome.is_palindrome("deified"))
        self.assertTrue(palindrome.is_palindrome("civic"))
        self.assertTrue(palindrome.is_palindrome("radar"))
        self.assertTrue(palindrome.is_palindrome("level"))

        self.assertTrue(palindrome.is_palindrome("Mr Owl ate my metal worm"))
        self.assertTrue(palindrome.is_palindrome("Do geese see God"))
        self.assertTrue(palindrome.is_palindrome("Was it a car or a cat I saw"))
        self.assertTrue(palindrome.is_palindrome("Murder for a jar of red rum"))

        self.assertFalse(palindrome.is_palindrome("palindrome"))
        self.assertFalse(palindrome.is_palindrome("Python"))
