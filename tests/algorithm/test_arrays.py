from unittest import TestCase
from algorithm.arrays import Arrays


class TestArrays(TestCase):
    def test_intersection_two_arrays_ii(self):
        # Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2]
        self.assertEqual(len(Arrays.intersection_two_arrays_ii(nums1=[1, 2, 2, 1], nums2=[2, 2])), 2)

        # nums1 =[3,1,2], nums2 = [1,3], return [1,3]
        self.assertEqual(len(Arrays.intersection_two_arrays_ii(nums1=[3, 1, 2], nums2=[1, 3])), 2)

        # Test with spaces

        # Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2]
        self.assertEqual(len(Arrays.intersection_two_arrays_ii_with_space(nums1=[1, 2, 2, 1], nums2=[2, 2])), 2)

        # nums1 =[3,1,2], nums2 = [1,3], return [1,3]
        self.assertEqual(len(Arrays.intersection_two_arrays_ii_with_space(nums1=[3, 1, 2], nums2=[1, 3])), 2)

    def test_find_duplicates(self):
        # [4,3,2,7,8,2,3,1] => [2,3]
        self.assertListEqual(Arrays.find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]), [2, 3])

        # [2,2] => [2]
        self.assertListEqual(Arrays.find_duplicates([2, 2]), [2])

    def test_product_except_self(self):
        # Input:  [1,2,3,4] => Output: [24,12,8,6]
        self.assertListEqual(Arrays.product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])

        # [1,2] => [2,1]
        self.assertListEqual(Arrays.product_except_self([1, 2]), [2, 1])

        # [1,2,3] => [6,3,2]
        self.assertListEqual(Arrays.product_except_self([1, 2, 3]), [6, 3, 2])

        # [2,2] => [2,2]
        self.assertListEqual(Arrays.product_except_self([2, 2]), [2, 2])

    def test_combination_sum(self):
        """
        Input: candidates = [2,3,6,7], target = 7,
        A solution set is:
        [
          [7],
          [2,2,3]
        ]
        """
        a = Arrays()
        self.assertListEqual(a.combination_sum([2, 3, 6, 7], 7), [[7], [2, 2, 3]])
