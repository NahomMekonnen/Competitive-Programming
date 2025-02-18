# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ans =[]
        for i in range(len(nums)-1):
            if nums[i] == 0 :
                continue 
            if nums[i] == nums[i+1] :
                ans.append(nums[i] * 2)
                nums[i+1] = 0
            else :
                ans.append(nums[i])
        ans.append(nums[-1])
        return ans + [0] * (len(nums) - len(ans))