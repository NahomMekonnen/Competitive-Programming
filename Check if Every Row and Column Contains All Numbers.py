class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        rows, cols = defaultdict(set), defaultdict(set)
        for i in range(len(matrix)) :
            for j in range(len(matrix[i])) :
                rows[i+1].add(matrix[i][j])
                cols[j+1].add(matrix[i][j])
        for i in range(1,len(matrix)+1) :
            if len(rows[i]) != len(matrix) :
                return False
            if len(cols[i]) != len(matrix) :
                return False
        return True
