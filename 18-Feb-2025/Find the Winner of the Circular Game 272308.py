# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr, i = [i for i in range(1,n+1)], 0
        while len(arr) > 1 :
            i = (i + k-1) % len(arr)
            arr.pop(i)
        return arr[-1]
        

