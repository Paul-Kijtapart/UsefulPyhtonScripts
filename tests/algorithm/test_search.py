from unittest import TestCase
from algorithm.search import Search


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

    def test_contain_duplicate_ii(self):
        # Input: [1,2,3,1], k = 3 -> True
        self.assertTrue(Search.contain_duplicate_ii([1, 2, 3, 1], 3))

        # Input: [1,0,1,1], k = 1 -> True
        self.assertTrue(Search.contain_duplicate_ii([1, 0, 1, 1], 1))

        # Input: [1,2,1], k = 0 -> False
        self.assertFalse(Search.contain_duplicate_ii([1, 2, 1], 0))

    def test_search_range(self):
        self.assertListEqual(Search.search_range([5, 7, 7, 8, 8, 10], 8), [3, 4])

        self.assertListEqual(Search.search_range([5, 7, 7, 8, 8, 10], 5), [0, 0])

        self.assertListEqual(Search.search_range([5, 7, 7, 8, 8, 10], 6), [-1, -1])

        self.assertListEqual(Search.search_range([5, 7, 7, 8, 8, 10], 9), [-1, -1])

        self.assertListEqual(Search.search_range([5, 7, 7, 8, 8, 10], 10), [5, 5])

        self.assertListEqual(Search.search_range([5, 7, 7, 8, 8, 10], 13), [-1, -1])

        self.assertListEqual(Search.search_range([5, 7, 7, 8, 8, 10], 4), [-1, -1])

        self.assertListEqual(Search.search_range([], 0), [-1, -1])
