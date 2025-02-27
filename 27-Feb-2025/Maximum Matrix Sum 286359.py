# Problem: Maximum Matrix Sum - https://leetcode.com/problems/maximum-matrix-sum/description/?envType=problem-list-v2&envId=matrix

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        numNeg, minEl = 0, float("inf")
        ans = 0
        for row in matrix :
            for i in row :
                minEl = min(minEl, abs(i))
                if i < 0 :
                    numNeg += 1
                ans += abs(i)
        print(minEl)
        if numNeg % 2 == 1:
            ans -= minEl
            ans -= minEl
        return ans
        