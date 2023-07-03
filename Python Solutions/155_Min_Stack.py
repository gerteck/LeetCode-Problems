class MinStack:
    def __init__(self):
        self.stack = []

    # Keeps a pair of integers. Each pair consists of element
    # and the minimum element encountered so fair.
    def push(self, val: int) -> None:
        # If stack is empty
        if not self.stack:
            self.stack.append((val, val))
        else:
            mn = min(self.stack[-1][1], val)
            self.stack.append((val, mn))

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

            # Note [-1] means last element of sequence

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        return 0

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        return 0


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Answer accepted leetcode
