# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0 :
            return 0
        num_set , ans = set(nums), 0

        for num in num_set :
            if num - 1 not in num_set:
                cnt, start = 1, num # start of the sequence
                while start + 1 in num_set :
                    cnt += 1
                    start = start + 1
                ans = max(cnt, ans) 
        
        return ans