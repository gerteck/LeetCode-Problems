'''
The concept of a stack, a last-in/first-out construct, is integral to the left-to-right evaluation of RPN.
In the example 3 4 -, first the 3 is put onto the stack, then the 4; the 4 is now on top and the 3 below it.
The subtraction operator removes the top two items from the stack, performs 3 - 4, and puts the result of -1 onto the
stack.
'''

from typing import List

# For reverse polish notation, we use a stack to evaluate the sequence of tokens.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        while len(tokens) > 0:
            token = tokens.pop(0)
            if token == "+" or token == "-" or token == "*" or token == "/":
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())
                result = 0

                if token == "+":
                    result = operand1 + operand2
                elif token == "/":
                    result = operand1 / operand2
                elif token == "*":
                    result = operand1 * operand2
                elif token == "-":
                    result = operand1 - operand2

                # Round off:
                result = int(result)
                stack.append(result)
            else:
                stack.append(token)

        return int(stack.pop())


a = Solution()
print(a.evalRPN(["4","13","5","/","+"]))

# Verified Accepted Submission on Leetcode.