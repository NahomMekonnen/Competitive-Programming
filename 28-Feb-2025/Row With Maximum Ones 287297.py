# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ans = [0,0]
        for i in range (len(mat)):
            cnt = mat[i].count(1)
            if cnt > ans[1] :
                ans = [i,cnt]
        return ans
