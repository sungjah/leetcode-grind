class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        output = ""
        for s in words:
            l = 0
            r = len(s)-1
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                     break
            if l >= r:
                output = s
                break
        return output