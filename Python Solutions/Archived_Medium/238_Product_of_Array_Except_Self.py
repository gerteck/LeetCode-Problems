from typing import List

'''
Constraints: Must present an O(n) solution and 
must not use the division operation.
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # Have a prefix product and a postfix product
        prefix_product = []
        postfix_product = []

        length = len(nums)
        prefix = 1
        postfix = 1

        for i in range(length):
            prefix_product.append(prefix)
            prefix = prefix * nums[i]

        for i in range(length - 1, -1, -1):
            postfix_product.insert(0, postfix)
            postfix = postfix * nums[i]

        result = []

        for i in range(length):
            product = prefix_product[i] * postfix_product[i]
            result.append(product)

        return result


a = Solution()
print(a.productExceptSelf([-1,1,0,-3,3]))

# Solution verified and accepted Leetcode