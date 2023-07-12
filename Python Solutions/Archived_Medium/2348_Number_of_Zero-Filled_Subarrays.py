from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        total = 0
        number_of_subsequent_zeros = 0
        counter = 0

        for x in range(length):
            if nums[x] != 0:
                if number_of_subsequent_zeros > 0:
                    total += counter
                    counter = 0
                    number_of_subsequent_zeros = 0

            if nums[x] == 0:
                number_of_subsequent_zeros += 1
                counter += number_of_subsequent_zeros

        total += counter
        return total


# Verified Accepted Submission on LeetCode