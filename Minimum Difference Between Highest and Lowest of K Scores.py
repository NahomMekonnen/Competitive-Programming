class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = float("inf")
        nums.sort(reverse = True)
        for i in range(len(nums)) :
            if (i + k - 1) >= len(nums) :
                break
            ans = min(ans,nums[i] - nums[i+k-1])
        return ans
