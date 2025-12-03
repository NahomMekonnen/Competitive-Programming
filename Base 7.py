class Solution:
    def convertToBase7(self, num: int) -> str:
        sign = True if num < 0 else False
        if num == 0 :
            return str(num)
        ans = ""
        num = abs(num)
        while num :
            n = num % 7
            num //= 7
            ans += str(n)
        ans = ans[::-1]
        return "-" + ans if sign else ans
