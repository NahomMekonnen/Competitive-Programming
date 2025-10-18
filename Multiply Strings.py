class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0
        exp = 1
        for i in range(len(num1)-1,-1,-1) :
            n1 += (ord(num1[i]) - ord("0")) * exp
            exp *= 10
        exp = 1
        for i in range(len(num2)-1,-1,-1) :
            n2 += (ord(num2[i]) - ord("0")) * exp
            exp *= 10
        return str(n1*n2)
