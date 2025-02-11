# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        ans = [0,0]
        freq = Counter(nums)
        for i in freq:
            ans[0] += (freq[i]//2)
            ans[1] += (freq[i]%2)
        return ans
