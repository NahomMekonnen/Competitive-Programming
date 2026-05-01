class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        S = sum(nums)
        F = sum([i * el for i, el in enumerate(nums)])
        ans = F
        for i in range(1,n) :
            F = F + S - ( n * nums[n - i])
            ans = max(F, ans)
        return ans
