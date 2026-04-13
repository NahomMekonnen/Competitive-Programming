class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m = len(matrix)
        n = len(matrix[0])
        possible = [min(i) for i in matrix]
        for i in range(n) :
            l = 0
            for j in range(m) :
                l = max(l, matrix[j][i])
            if l in possible :
                ans.append(l)

        return ans 
