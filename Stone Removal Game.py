class Solution:
    def canAliceWin(self, n: int) -> bool:
        a = True
        for i in range(10, 0, -1) :
            n -= i
            if n < 0 :
                return False if a == True else True
            a = not a
        return True 

