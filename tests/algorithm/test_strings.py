from unittest import TestCase

from algorithm.strings import Strings


class TestStrings(TestCase):
    def test_find_the_difference(self):
        # s = "abcd", t = "abcde" => 'e'
        self.assertEqual(Strings.find_the_difference('abcd', 'abcde'), 'e')

        # s = "abcd", t = "abcde" => 'e'
        self.assertEqual(Strings.find_the_difference_pro('abcd', 'abcde'), 'e')
