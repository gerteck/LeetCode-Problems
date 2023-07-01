class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        dict = {}
        position = 0

        start = -1
        max_count = 0

        for char in s:
            print(char)
            if char not in dict:
                dict[char] = position
            else:
                start = max(start, dict[char])
                dict[char] = position

            length = position - start
            position += 1
            max_count = max(max_count, length)

        return max_count

a = Solution()
print(a.lengthOfLongestSubstring("abcabcabc"))

