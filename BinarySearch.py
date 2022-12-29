class Solution:
    def search(self, nums: List[int], target: int) -> int:
        firstHalf = 0
        secondHalf = len(nums) - 1

        while firstHalf <= secondHalf:
            m = firstHalf + ((secondHalf -1) // 2)
            if nums[m] > target:
                secondHalf = m - 1
            elif nums[m] < target:
                firstHalf = m + 1
            else:
                return m
        return -1