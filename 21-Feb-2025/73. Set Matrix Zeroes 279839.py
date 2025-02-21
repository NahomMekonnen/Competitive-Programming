# Problem: 73. Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        pos = []
        rowSize,colSize = len(matrix), len(matrix[0])
        for r in range(rowSize) :
            for c in range(colSize) :
                if matrix[r][c] == 0:
                    pos.append([r,c])
        for i in pos :
            row, col = i[0], i[1]
            matrix[row] = [0] * colSize
            for r in range(rowSize) :
                matrix[r][col] = 0

            