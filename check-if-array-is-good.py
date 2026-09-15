class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        nums.sort()

        n = len(nums) - 1

        for i in range(n - 1):
            if nums[i] != i + 1:
                return False

        return nums[n - 1] == n and nums[n] == n