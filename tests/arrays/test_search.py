from unittest import TestCase
from algorithm.arrays.search import Search


class TestSearch(TestCase):

    def test_search_rotated_array(self):
        # empty cases
        empty_nums = []
        self.assertEqual(Search.search_rotated_array(empty_nums, 80), -1)

        # sorted left side
        left_sorted_nums = [50, 80, 100, 10, 30]

        left_in_target = 50
        self.assertNotEqual(Search.search_rotated_array(left_sorted_nums, left_in_target), -1)

        right_in_target = 10
        self.assertNotEqual(Search.search_rotated_array(left_sorted_nums, right_in_target), -1)

        left_out_target = 60
        self.assertEqual(Search.search_rotated_array(left_sorted_nums, left_out_target), -1)

        right_out_target = 40
        self.assertEqual(Search.search_rotated_array(left_sorted_nums, right_out_target), -1)

        # sorted right side
        right_sorted_nums = [80, 100, 10, 30, 50]

        left_in_target = 100
        self.assertNotEqual(Search.search_rotated_array(right_sorted_nums, left_in_target), -1)

        right_in_target = 30
        self.assertNotEqual(Search.search_rotated_array(right_sorted_nums, right_in_target), -1)

        left_out_target = 70
        self.assertEqual(Search.search_rotated_array(right_sorted_nums, left_out_target), -1)

        right_out_target = 40
        self.assertEqual(Search.search_rotated_array(right_sorted_nums, right_out_target), -1)

        # left duplicate nums
        left_duplicate_nums = [10, 10, 10, 30, 50]

        left_in_target = 10
        self.assertNotEqual(Search.search_rotated_array(left_duplicate_nums, left_in_target), -1)

        right_in_target = 50
        self.assertNotEqual(Search.search_rotated_array(left_duplicate_nums, right_in_target), -1)

        left_out_target = 0
        self.assertEqual(Search.search_rotated_array(left_duplicate_nums, left_out_target), -1)

        right_out_target = 100
        self.assertEqual(Search.search_rotated_array(left_duplicate_nums, right_out_target), -1)

        # all duplicate
        duplicate_nums = [10, 10, 10, 10, 10]

        left_in_target = 10
        self.assertNotEqual(Search.search_rotated_array(left_duplicate_nums, left_in_target), -1)

        right_in_target = 10
        self.assertNotEqual(Search.search_rotated_array(left_duplicate_nums, right_in_target), -1)

        left_out_target = 0
        self.assertEqual(Search.search_rotated_array(left_duplicate_nums, left_out_target), -1)

        right_out_target = 100
        self.assertEqual(Search.search_rotated_array(left_duplicate_nums, right_out_target), -1)
