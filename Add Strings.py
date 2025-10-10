class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0
        pow = 1
        for i in num1[::-1] :
            n1 += (pow * int(i))
            pow *= 10
        pow = 1
        for i in num2[::-1]:
            n2 += (pow * int(i))
            pow *= 10
        add = n1 + n2
        if add == 0 :
            return "0"
        ans = ""
        while add : 
            ans += str(add%10)
            add//=10
        return ans[::-1]
