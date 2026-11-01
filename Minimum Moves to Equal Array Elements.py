class Solution:
    def minMoves(self, nums: list[int]) -> int:
        m, ans = min(nums), 0
        for i in nums :
            ans += i - m
        return ans