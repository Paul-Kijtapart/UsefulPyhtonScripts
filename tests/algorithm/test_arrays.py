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
