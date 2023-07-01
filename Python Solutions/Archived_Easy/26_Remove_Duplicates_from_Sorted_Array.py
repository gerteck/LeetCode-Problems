class Solution:

    # Approach: Have two pointers, a placement pointer and a reference pointer.
    # Placement pointer will reference the last updated position
    # Reference pointer will loop through array

    def removeDuplicates(self, nums: [int]) -> int:
        placement = 0
        reference = 0

        prev_num = None
        length = len(nums)

        for number in nums:
            if prev_num is None:
                prev_num = number
                placement += 1

            if number != prev_num:
                prev_num = number
                nums[placement] = number
                placement += 1

        return placement


s = Solution()
int_array = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6, 7, 8, 8, 8, 8, 9]
print("Unique Numbers: " + str(s.removeDuplicates(int_array)))
print(int_array)