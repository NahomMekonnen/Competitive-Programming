class Solution:
    # adding comments cuz this one of the most confusing questions to implement
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        row, col = len(matrix), len(matrix[0])
        layers = (min(col,row) + 1) // 2
        for i in range(layers) :
            # horizontal traversal top left to top right
            for h in range(i, col - i) :
                ans.append(matrix[i][h])
            # vertical traversal top left to bottom left
            for v in range(i + 1, row - i) :
                ans.append(matrix[v][col - 1 - i])
            # horizontal traversal bottom right to bottom left
            if row - 1 - i != i :
                for h in range(col - 2 - i, i - 1, -1) :
                    ans.append(matrix[row - 1 - i][h])
            # vertical traversal bottom left to top left 
            if col - 1 - i != i :
                for v in range(row - 2 - i, i, -1) :
                    ans.append(matrix[v][i])
        return ans
