
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        averages = []
        nums.sort()
        l, r = 0, len(nums) - 1
        while l < r :
            averages.append((nums[l] + nums[r])/2)
            l += 1
            r -= 1
        return len(set(averages))
