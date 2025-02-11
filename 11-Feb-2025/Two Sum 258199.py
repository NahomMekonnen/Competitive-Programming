# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = dict()
        for i in range(len(nums)):
            search = target - nums[i]
            if search in indices:
                return [i, indices[search]]
            indices[nums[i]] = i
        return []
        