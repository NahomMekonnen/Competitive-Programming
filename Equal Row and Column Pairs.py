class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = defaultdict(int)
        for i in range(len(grid[0])) :
            col = []
            for j in range(len(grid)) :
                col.append(grid[j][i])
            cols[tuple(col)] += 1
        ans = 0
        for row in grid :
            if cols[tuple(row)] :
                ans += 1 * cols[tuple(row)]
        return ans
