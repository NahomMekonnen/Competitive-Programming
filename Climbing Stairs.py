class Solution:
    def climbStairs(self, n: int) -> int:
        current, previous = 1, 1
        for i in range(1, n) :
            current, previous = current + previous, current
        return current
        
