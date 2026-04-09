class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        n = sorted([i for i in nums if i < 0 ])
        for i in n :
            if abs(i) in nums :
                return abs(i)
        return  -1
