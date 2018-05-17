from collections import Counter


class Arrays:

    @staticmethod
    def intersection_two_arrays_ii(nums1: list, nums2: list) -> list:
        """

        Args:
            nums1(list(int): list of unsorted numbers
            nums2(list(int): list of unsorted numbers

        Returns:
            list(int): list of overlapped numbers from the given 2 lists

        """

        res = []

        # sort both nums1 and nums2 in-place
        nums1.sort()
        nums2.sort()

        # construct overlapped list of numbers from the 2 sorted list

        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):

            if nums1[i] == nums2[j]:
                res.append(nums2[j])

                i += 1
                j += 1
            elif nums1[i] > nums2[j]:

                j += 1

                # move j to next number
                while j < len(nums2):
                    if j != 0 and nums2[j] != nums2[j - 1]:
                        break

                    j += 1

            # if nums[1] < nums2[j]
            else:
                i += 1

                # move j to next number
                while i < len(nums1):
                    if i != 0 and nums1[i] != nums1[i - 1]:
                        break

                    i += 1

        return res

    @staticmethod
    def intersection_two_arrays_ii_with_space(nums1: list, nums2: list) -> list:
        """

               Args:
                   nums1(list(int): list of unsorted numbers
                   nums2(list(int): list of unsorted numbers

               Returns:
                   list(int): list of overlapped numbers from the given 2 lists

        """

        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

        # determine overlapping keys
        overlapped_keys = [k1 for k1 in counter1 if k1 in counter2]

        # Generate overlapped values as many times as possible for the overlapped keys
        res = []

        for key in overlapped_keys:
            vals = [key] * min(counter1.get(key), counter2.get(key))
            res += vals

        return res

    @staticmethod
    def find_duplicates(nums):
        """
        Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
        Find all the elements that appear twice in this array.
        Could you do it without extra space and in O(n) runtime?

        Args:
            nums(List[int]):

        Returns:
            List[int] - list of duplicates found in the nums

        """

        duplicates = []

        # loop through nums to find all duplicates

        for num in nums:

            mark_index = abs(num) - 1

            if nums[mark_index] < 0:
                duplicates.append(abs(num))
            else:
                nums[mark_index] *= -1

        return duplicates

    @staticmethod
    def product_except_self(nums: list) -> list:
        """
        Given an array nums of n integers where n > 1,
        return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

        Args:
            nums(List[int]): list of number with n size, n > 1

        Returns:
            List[int]

        """

        # build product of left except self
        product_left = list(nums)

        # set first one as = 1
        product_left[0] = 1

        for i in range(1, len(nums)):
            product_left[i] = product_left[i - 1] * nums[i - 1]

        # build product of right except self
        product_right = list(nums)

        # set last one as = 1
        product_right[len(nums) - 1] = 1

        for i in reversed(range(len(nums) - 1)):
            product_right[i] = product_right[i + 1] * nums[i + 1]

        # build product of the two above
        res = []

        for i in range(len(nums)):
            res.append(product_right[i] * product_left[i])

        return res

    def combination_sum_helper(self, candidates, target, index, comb, arrays):
        # base case
        if index >= len(candidates):
            return True  # done exit

        num = candidates[index]

        # Visit this node

        target -= num

        # update comb first
        if target < 0:
            return True
        else:
            comb.append(num)

        # update arrays if possible
        if target == 0:
            arrays.append(list(comb))
            comb.pop()
            return True

        for i in range(index, len(candidates)):
            should_exit = self.combination_sum_helper(candidates=candidates,
                                                      target=target,
                                                      index=i,
                                                      comb=comb,
                                                      arrays=arrays)

            if should_exit:
                break

        # take the num out
        comb.pop()

    def combination_sum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        candidates.sort()

        all_combs = []

        for index in range(len(candidates)):
            self.combination_sum_helper(candidates, target, index, [], all_combs)

        return all_combs

    @staticmethod
    def get_unique_combinations(combs):

        visited_counter = set()

        for comb in combs:

            key = Counter(comb)

            if key not in visited_counter:
                visited_counter[key] = comb

        return list(visited_counter)
