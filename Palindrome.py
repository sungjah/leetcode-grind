class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        temp = 1;
        for index, char in enumerate(strx):
            if strx[0] == "-":
                return False
            if strx[index] == strx[len(strx)-temp]:
                index += 1
                temp +=1
            else:
                return False
        return True

class FollowUpSolution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        div = 1
        while x >= 10 * div:
            div *= 10
        while x:
            right = x % 10
            left = x // div
            if left != right:
                return False
            x = x % div // 10
            div = div / 100
        return True

