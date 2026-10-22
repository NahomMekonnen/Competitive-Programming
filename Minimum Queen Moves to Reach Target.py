class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        if source == target :
            return 0
        if abs(source[0] - target[0]) == abs(target[-1] - source[-1]) :
            return 1 
        ans = 0
        if source[0] != target[0] :
            ans += 1
        if source[1] != target[1] :
            ans += 1
        return ans