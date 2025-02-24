# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols -1
        while left <= right :
            mid = left + (right - left)//2
            val = matrix[mid//cols][mid%cols]
            if val == target :
                return True
            elif val > target :
                right = mid - 1
            else :
                left = mid + 1
        return False