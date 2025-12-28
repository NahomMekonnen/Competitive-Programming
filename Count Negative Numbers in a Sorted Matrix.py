class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in grid :
            for j in range(len(i)-1,-1,-1) :
                if i[j] >= 0:
                    break
                ans += 1
        return ans
