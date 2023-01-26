class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def generate(result: List[str], s: str, _open: int, close: int, n: int):
            # Base condition
            if _open == n and close == n:
                result.append(s)
                return
            # If the number of _open parentheses is less than the given n
            if _open < n:
                generate(result, s + "(", _open + 1, close, n)
            # If we need more close parentheses to balance
            if close < _open:
                generate(result, s + ")", _open, close + 1, n)

        generate(result, "", 0, 0, n)
        return result
