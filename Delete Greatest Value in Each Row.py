class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)) :
            grid[i].sort()
        ans = 0
        s = len(grid[0])
        for j in range(s) :
            add = 0 
            for i in range(len(grid)) :
                add = max(add, grid[i][-1])
                grid[i].pop()
            ans += add
        return ans
