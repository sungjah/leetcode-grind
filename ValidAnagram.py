class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        storage = []
        for c in s:
            storage.append(c)
        for c2 in t:
            if c2 in storage:
                storage.remove(c2)
            else:
                return False
        if not storage:
            return True