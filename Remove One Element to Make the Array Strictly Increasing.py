class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)) :
            arr = nums[:i] + nums[i+1:]
            if len(arr) != len(set(arr)) :
                continue
            if arr == sorted(arr) :
                return True
        return False
