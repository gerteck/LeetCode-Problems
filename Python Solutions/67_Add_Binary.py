class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Convert both numbers to integers using python library
        result = int(a, 2) + int(b, 2)
        return format(result, 'b')


s = Solution()
print(s.addBinary("100", "010"))
