class Solution:
    def coloredCells(self, n: int) -> int:
        ans, add = 1, 0
        for i in range(n) :
            ans += add
            add += 4 
        return ans
