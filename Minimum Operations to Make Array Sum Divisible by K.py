class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        m = sum(nums) % k 
        if m == 0 : 
            return 0
        if m < k :
            return m
        return m - k
