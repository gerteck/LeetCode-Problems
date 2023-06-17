# 169: Majority Element; Easy Difficulty
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

class Solution:

    # self is referring to the solution instance
    # nums: List[int]
    def majorityElement(self, nums) -> int:
        number_dict = {}
        if len(nums) == 1:
            return nums[0]

        # Math floor using int data type
        majority_count = int(len(nums)/2)

        for number in nums:
            count = number_dict.get(number)
            if count is None:
                number_dict[number] = 1
            elif ++count >= majority_count:
                return number
            else:
                number_dict[number] = count + 1

        return 0


test = Solution()
print(test.majorityElement([4, 4, 4, 2, 1]))


