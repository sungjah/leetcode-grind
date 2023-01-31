class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        storage = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in storage and i - storage[num] <= k:
                return True
            storage[num] = i

        return False
