class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for row in nums :
            row.sort()
        ans = 0
        idx = len(nums[0])
        while idx :
            score = 0
            for i in nums :
                score = max(score,i[-1])
                i.pop()
            ans += score
            idx -= 1
        return ans
