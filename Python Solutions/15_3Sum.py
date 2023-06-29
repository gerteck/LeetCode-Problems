from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array
        nums.sort()
        # to return later
        res = []

        for i, a in enumerate(nums):
            # if its not the first number and is equal to previous number then continue
            if i > 0 and nums[i] == nums[i-1]: continue
            # rest of the problem is similar to two sum II
            # two sum II
            l, r = i+1, len(nums)-1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0: r -= 1
                elif threesum < 0: l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    # increment the left pointer
                    l += 1

                    # while both pointer arent equal and not crossing each other
                    # and while num is same as prev num,
                    # keep incrementing the left pointer
                    while l < r and nums[l] == nums[l-1]: l += 1
        # lastly return the res array
        return res


# Notes: Solution set cannot contain duplicate triplets. (Cannot use same positional number)
# Approach: have three pointers and iterate through array
# Solution cannot contain duplicate triplets. Hence, we can sort the array.

a = Solution()
print(a.threeSum([-1,0,1,2,-1,-4]))