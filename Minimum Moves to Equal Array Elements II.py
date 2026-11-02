class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        if len(nums) == 1 :
            return 0
        ans = 0
        nums.sort()
        mid = len(nums) // 2
        if len(nums) % 2 == 0 :
            mid -= 1
        for i in nums :
            ans += abs(i - nums[mid])

        return ans

