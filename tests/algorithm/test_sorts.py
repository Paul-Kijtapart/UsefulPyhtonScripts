from unittest import TestCase
from algorithm.sorts import Sorts


class TestSorts(TestCase):

    def test_sort_anagram(self):
        # empty array
        empty_array = []
        self.assertListEqual(Sorts.sort_anagram(empty_array), [])

        # array with words
        words = ["abc", "deg", "bca", "gg", "egd"]
        self.assertListEqual(Sorts.sort_anagram(words), ["abc", "bca", "deg", "egd", "gg"])