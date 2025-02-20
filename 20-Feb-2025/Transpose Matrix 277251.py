# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(matrix[0])) :
            column = []
            for j in range(len(matrix)) :
                column.append(matrix[j][i])
            ans.append(column)
        return ans