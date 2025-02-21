# Problem: Maximum Sum of an Hourglass - LeetCode - https://leetcode.com/problems/maximum-sum-of-an-hourglass/description/

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxSum = 0 
        for i in range(len(grid)-2) :
            for j in range(len(grid[0])-2):
                total = 0
                total += grid[i][j] + grid[i][j+1] + grid[i][j+2] # first row
                total += grid[i+1][j+1] # hourglass
                total += grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] # third row
                maxSum = max(maxSum, total)
        return maxSum