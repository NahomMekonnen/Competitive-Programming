class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles 
        empty = ans
        while empty >= numExchange :
            left = empty % numExchange
            empty //= numExchange
            ans += empty
            empty += left
        return ans
