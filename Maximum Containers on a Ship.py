class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        maxCells = n * n
        return maxCells if maxCells * w  < maxWeight else maxWeight//w
        
        