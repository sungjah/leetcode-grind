class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        storage = set()
        for n in nums:
            if n not in storage:
                storage.add(n)
            else:
                return True
        return False