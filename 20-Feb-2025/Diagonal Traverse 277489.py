# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        map, longest = defaultdict(deque), 0
        for i in range(len(mat)) :
            for j in range(len(mat[i])) :
                if (i+j) % 2 == 0:
                    map[i+j].append(mat[i][j])
                else :
                    map[i+j].appendleft(mat[i][j])
                longest = max(i+j,longest)
        ans = []
        for i in range(longest+1):
            while len(map[i])>0 :
                ans.append(map[i].pop())
        return ans