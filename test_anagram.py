import unittest
import anagram

class TestAnagram(unittest.TestCase):

    def test_is_anagram(self):
        self.assertTrue(anagram.is_anagram("pat", "tap"))
        self.assertTrue(anagram.is_anagram("angered", "enraged"))
        self.assertTrue(anagram.is_anagram("evil", "vile"))
        self.assertTrue(anagram.is_anagram("debit card", "bad credit"))
        self.assertFalse(anagram.is_anagram("  ", " "))
        self.assertFalse(anagram.is_anagram("cat", "dog"))
        self.assertFalse(anagram.is_anagram("Man", "man"))


if __name__ == '__main__':
    unittest.main()