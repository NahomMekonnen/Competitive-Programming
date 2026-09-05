class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        maxs, mins = [0] * len(nums), [0] * len(nums)
        currmax, currmin = 0, float("inf")
        for i in range(len(nums)) :
            currmax = max(currmax, nums[i])
            maxs[i] = currmax
        for i in range(len(nums) - 1, -1, -1) :
            currmin = min(currmin, nums[i])
            mins[i] = currmin
        for i in range(len(maxs)) :
            if maxs[i] - mins[i] <= k :
                return i
        return -1
