class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        ans = 0
        m = len(grid)
        for row in range(m) :
            num = grid[row].count(1)
            if num > 1 :
                ans += num
            elif num == 1 :
                idx = grid[row].index(1)
                for r in range(m) :
                    if r != row and grid[r][idx] == 1 :
                        ans += 1
                        break
        return ans
