class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drunk = empty = numBottles
        full = 0
        exc = numExchange
        while True:
            if empty < exc :
                break
            while empty >= exc :
                full += 1
                empty -= exc
                exc += 1
            drunk += full
            empty += full
            full = 0
        return drunk
