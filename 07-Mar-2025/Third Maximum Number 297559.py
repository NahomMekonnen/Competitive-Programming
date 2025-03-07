# Problem: Third Maximum Number - https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        return sorted(list(set(nums)))[-3 if len(sorted(list(set(nums)))) >= 3 else -1]