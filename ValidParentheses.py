class Solution:
    def isValid(self, s: str) -> bool:
        emptyStack = []
        openingP = ["(", "{", "["]
        for x in s:
            if x in openingP:
                emptyStack.append(x)
            else:
                if not emptyStack:
                    return False
                if x == ")" and emptyStack[-1] != "(":
                    return False
                if x == "}" and emptyStack[-1] != "{":
                    return False
                if x == "]" and emptyStack[-1] != "[":
                    return False
                emptyStack.pop()
        return len(emptyStack) == 0