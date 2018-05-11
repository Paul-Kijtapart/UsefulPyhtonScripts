class Search:

    @staticmethod
    def search_rotated_array(nums: list, target: int) -> int:
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

                if target < current_num:
                    return -1
                else:
                    # go right
                    left = mid_index + 1

        # if NOT found
        return -1

    @staticmethod
    def contain_duplicate_ii(nums: list, k: int) -> bool:
        """Check if the given num has any duplicate within k distance

        Args:
            nums(list.<int>): list of numbers
            k(int): distance to search for duplicate from each position

        Returns:
            bool:   True if found duplicate within k
                    otherwise, False.

        """
        if len(nums) == 0 or k < 1:
            return False

        # Map to keep track of last-seen position of each number in nums
        num_prev_position = dict()

        for i, num in enumerate(nums):

            if num in num_prev_position:

                # last-seen position
                prev_position = num_prev_position[num]

                # if we found duplicate within k distance
                if i - prev_position <= k:
                    return True

                # if distance > k, update prev_position
                num_prev_position[num] = i

            else:

                num_prev_position[num] = i

        # if not found any duplicate
        return False
