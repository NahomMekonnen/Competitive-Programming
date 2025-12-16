class Solution:
    def isFascinating(self, n: int) -> bool:
        num = str(n) + str(2*n) + str(3*n)
        if '0' in num :
            return False
        return True if len(set(num)) == len(num) == 9 else False
