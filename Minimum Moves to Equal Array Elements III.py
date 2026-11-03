class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m, ans = max(nums), 0
        for i in nums :
            ans += m - i
        return ans