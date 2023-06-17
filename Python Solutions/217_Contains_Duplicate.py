class Solution:
    def containsDuplicate(self, nums) -> bool:
        # nums it the list / Array of numbers
        # sort the array then check
        sorted_nums = nums
        sorted_nums.sort()
        prev_num = sorted_nums[0]
        sorted_nums.pop(0)
        for num in sorted_nums:
            if (num == prev_num):
                return True
            prev_num = num

        return

    # Approach: Sort the array and check if any consecutive element is the same.
    # If there are same elements, they would be next to each other and hence
    # would mean that the array contains a duplicate


test = Solution()

print(test.containsDuplicate([4, 4, 3, 2, 1]))
