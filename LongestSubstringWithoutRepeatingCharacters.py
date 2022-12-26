class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = set()
        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in subString:
                subString.remove(s[l])
                l += 1
            subString.add(s[r])
            result = max(result, r - l + 1)
        return result