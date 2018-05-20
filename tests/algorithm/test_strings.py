from unittest import TestCase

from algorithm.strings import Strings


class TestStrings(TestCase):
    def test_find_the_difference(self):
        # s = "abcd", t = "abcde" => 'e'
        self.assertEqual(Strings.find_the_difference('abcd', 'abcde'), 'e')

        # s = "abcd", t = "abcde" => 'e'
        self.assertEqual(Strings.find_the_difference_pro('abcd', 'abcde'), 'e')

    def test_is_isomorphic(self):
        # Input: s = "egg", t = "add"

        # Input: s = "foo", t = "bar"

        # Input: s = "paper", t = "title"

        # Input: s = "ab", t = "aa" => False

        # Input: s = "aa", t = "ab" => False
        pass
