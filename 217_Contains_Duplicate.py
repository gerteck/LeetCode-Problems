class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # nums it the list / Array of numbers
        # sort the array then check 
        sorted_nums = nums.sort()
        prev_num = sorted_nums[0]
        sorted_nums.pop(0)
        for num in sorted_nums:
            if (num == prev_num):
                return True
            prev_num = num

        return False
