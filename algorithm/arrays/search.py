class Search:

    @staticmethod
    def search_rotated_array(nums, target):
        """

        Args:
            nums(int[]): list of numbers
            target(int): target number to search in nums

        Returns:
            int: index of the target in nums. Otherwise, -1

        """

        # if nums is empty
        if len(nums) == 0:
            return -1

        # if nums is NOT empty

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid_index = left + (right - left) // 2

            current_num = nums[mid_index]

            # if found target
            if current_num == target:
                return mid_index

            # if left side is sorted
            if current_num > nums[left]:

                # if target falls in range of left side
                if nums[left] <= target < current_num:
                    # go left
                    right = mid_index - 1

                # if target NOT falls in left side
                else:
                    # go right
                    left = mid_index + 1

            # if right side is sorted
            elif current_num < nums[left]:

                # if target falls in Right side
                if nums[right] >= target > current_num:
                    # go right
                    left = mid_index + 1

                # if target NOT falls in Right side
                else:
                    # go left
                    right = mid_index - 1

            # if left side is duplicate
            else:

                # go right
                left = mid_index + 1

        # if NOT found
        return -1
