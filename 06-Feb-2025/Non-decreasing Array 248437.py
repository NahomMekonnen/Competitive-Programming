# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        cnt  = 0  # count of violations 
        for i in range(1,len(nums)):
            if (nums[i-1] > nums[i]):
                if cnt > 0:
                    return False
                cnt += 1
                if i >= 2 and nums[i-2] >nums[i]:
                    nums[i] = nums[i-1]
        return True