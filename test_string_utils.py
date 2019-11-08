import unittest
import string_utils


class TestStringUtils(unittest.TestCase):

    def test_str_len(self):
        self.assertEqual(7, string_utils.str_len("roberto"))
        self.assertEqual(4, string_utils.str_len("yoda"))

    def test_first_char(self):
        self.assertEqual("r", string_utils.first_char("roberto")) 
        self.assertEqual("y", string_utils.first_char("yoda"))

    def test_last_char(self):
        self.assertEqual("o", string_utils.last_char("roberto")) 
        self.assertEqual("a", string_utils.last_char("yoda"))

    def test_input_has_substring(self):
        self.assertTrue(string_utils.input_has_substring("Roberto", "Rob"))
        self.assertFalse(string_utils.input_has_substring("Yoda", "Dark"))

    def test_substring(self):
        self.assertEqual("rob", string_utils.substring("roberto", 0, 3)) 
        self.assertEqual("da", string_utils.substring("yoda", 2, 4))

    def test_opposite_case(self):
        self.assertEqual("rOB", string_utils.opposite_case("Rob"))
        self.assertEqual("yoda", string_utils.opposite_case("YODA"))


if __name__ == '__main__':
    unittest.main()