# Intuition behind the idea:
# Have a counter for max count
# As we go through the array, we check:
# If prev + current > 0, keep prev

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_count = nums[0]
        count = 0
        if len(nums) == 1:
            return nums[0]

        for num in nums:
            if count < 0:
                count = num
            else:
                count += num

            if count > max_count:
                max_count = count

        return max_count



