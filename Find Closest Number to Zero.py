class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        nums.sort()
        if nums[0] > 0 :
            return nums[0]
        if nums[-1] < 0 :
            return nums[-1]
        diff = float('inf')
        prev = 0
        for i in nums :
            diff = min(diff, abs(i))
            if abs(i) == diff :
                prev = i
        return prev