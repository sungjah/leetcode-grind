class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        for c in s:
            if c.isalnum():
                newString += c.lower()
        return newString == newString[::-1]


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        pointerL = 0
        pointerR = len(s) - 1

        while pointerL < pointerR:
            while pointerL < pointerR and not self.alphaNum(s[pointerL]):
                pointerL += 1
            while pointerR > pointerL and not self.alphaNum(s[pointerR]):
                pointerR -= 1

            if s[pointerL].lower() != s[pointerR].lower():
                return False
            pointerL = pointerL + 1
            pointerR = pointerR - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
