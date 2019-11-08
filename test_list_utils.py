import unittest
import unittest.mock
from io import StringIO
import list_utils


class ListUtilsTest(unittest.TestCase):

    def test_get_item_at_position(self):
        list_in = ['Bicycle', 'Scooter', 'Motorcycle', 'Car', 'Jet ski', 'RV', 'Motorboat']
        self.assertEqual('Bicycle', list_utils.get_item_at_position(list_in, 0))
        self.assertEqual('Scooter', list_utils.get_item_at_position(list_in, 1))
        self.assertEqual('Motorcycle', list_utils.get_item_at_position(list_in, 2))
        self.assertEqual('Car', list_utils.get_item_at_position(list_in, 3))
        self.assertEqual('Jet ski', list_utils.get_item_at_position(list_in, -3))
        self.assertEqual('RV', list_utils.get_item_at_position(list_in, -2))
        self.assertEqual('Motorboat', list_utils.get_item_at_position(list_in, -1))

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_print_list_items(self, mock_stdout):
        list_in = ['one', 'two', 'three', 'four']
        list_utils.print_list_items(list_in)
        self.assertEqual("\n".join(list_in) + "\n", mock_stdout.getvalue())

    def test_sort_by_commit_count(self):
        list_in = [
            ['joe', 15],
            ['alice', 30],
            ['jane', 28],
            ['bob', 42]
        ]

        expected_out = [
            ['joe', 15],
            ['jane', 28],
            ['alice', 30],
            ['bob', 42]
        ]

        self.assertEqual(expected_out, list_utils.sort_by_commit_count(list_in))

    def test_gen_list_of_nums(self):
        expected_out = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(expected_out, list_utils.gen_list_of_nums(10))

    def test_half_list(self):
        list_in = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_out = [0, 1, 2, 3, 4]
        self.assertEqual(expected_out, list_utils.half_list(list_in, 1))

        list_in = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_out = [5, 6, 7, 8, 9]
        self.assertEqual(expected_out, list_utils.half_list(list_in, 2))

        list_in = [0, 1, 2, 3, 4]
        expected_out = [0, 1, 2]
        self.assertEqual(expected_out, list_utils.half_list(list_in, 1))

        list_in = [0, 1, 2, 3, 4]
        expected_out = [2, 3, 4]
        self.assertEqual(expected_out, list_utils.half_list(list_in, 2))

    def test_remove_odds(self):
        list_in = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_out = [0, 2, 4, 6, 8]
        list_utils.remove_odds(list_in)
        self.assertEqual(expected_out, list_in)

    def test_remove_evens(self):
        list_in = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        expected_out = [1, 3, 5, 7, 9]
        list_utils.remove_evens(list_in)
        self.assertEqual(expected_out, list_in)

    def test_concatenate_lists(self):
        self.assertEqual([1, 2, 1, 2], list_utils.concatenate_lists([1, 2], [1, 2]))
        self.assertEqual([1, 2, 3, 4, 5, 6], list_utils.concatenate_lists([1, 2, 3], [4, 5, 6]))
        self.assertEqual(['A', 'B', 'C', 'D', 'E', 'F'], list_utils.concatenate_lists(['A', 'B', 'C'], ['D', 'E', 'F']))
        fruits = ['apples', 'bananas']
        vegetables = ['tomato', 'carrot']
        self.assertEqual(['apples', 'bananas', 'tomato', 'carrot'], list_utils.concatenate_lists(fruits, vegetables))

    def test_multiply_list(self):
        self.assertEqual([1, 1, 1], list_utils.multiply_list([1], 3))
        self.assertEqual(['a', 'a', 'a', 'a'], list_utils.multiply_list(['a'], 4))
