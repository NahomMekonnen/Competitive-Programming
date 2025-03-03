# Problem: Max Number of K-Sum Pairs - https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i, j, op = 0, len(nums) - 1, 0 

        while i < j : 
            check = nums[i] + nums[j]
            if check == k :
                op += 1
                i += 1
                j -= 1
            elif check < k :
                i += 1
            else :
                j -= 1
        return op