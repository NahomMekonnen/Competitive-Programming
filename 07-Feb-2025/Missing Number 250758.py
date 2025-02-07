# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n , total = len(nums) , sum(nums)
        n *= (n+1)
        n //= 2
        return n - total