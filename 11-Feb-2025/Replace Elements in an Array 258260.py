# Problem: Replace Elements in an Array - https://leetcode.com/problems/replace-elements-in-an-array/

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        idx = dict()
        for i in range(len(nums)):
            idx[nums[i]] = i
        for op in operations:
            idx[op[1]] = idx[op[0]]
            idx.pop(op[0])
        for i in idx:
            nums[idx[i]] = i
        return nums