# Given an integer array nums and an integer k, return true
# if there are two distinct indices i and j in the array such that
# nums[i] == nums[j] and abs(i - j) <= k.

#                .     .
# Input: nums = [1,2,3,1], k = 3
# Output: true
# i - j <= k

# from typing import List
# Naive Solution
# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#       length = len(nums)
#       if length == 0:
#         return False

#       # Helper checks the next k positions to see if nums[i] == nums[j]
#       def helper(index):
#         value = nums[index]
#         for i in range(1, k + 1):
#           pointer = index + i
#           if pointer < length:
#             if nums[pointer] == value:
#               return True
#         return False

#       # Loop through array and apply helper.
#       for x in range(length):
#         if helper(x):
#           return True

#       return False

# Approach will be to store the last position of each number inside a hashmap
# When we iterate through the array, we check for the last position of the value.
# If the position is less or equal to k spots before the index, then return True

# Note is that we dont have to keep all the values, just update as the closest one will always
# be the updated one

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
      length = len(nums)
      dict = {}
      for x in range(length):
        value = nums[x]
        last_position = dict.get(value)
        if last_position is not None:
          if (x - last_position) <= k:
            return True
        dict[value] = x

      return False

a = Solution()
print("2", a.containsNearbyDuplicate([1,2,3,1], 3))
# Returns true