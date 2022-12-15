class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in hashmap:
                return [hashmap[difference], i]
            hashmap[n] = i

