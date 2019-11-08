import unittest
import unittest.mock
from io import StringIO
import list_utils


class ListUtilsTest(unittest.TestCase):

    def test_return_item_at_position(self):
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

