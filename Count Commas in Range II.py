class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000 :
            return 0
        if 10 ** 3 <= n < 10 ** 6 :
            return n - 999
        if 10 ** 6 <= n < 10 ** 9 :
            return n - 999999 + n - 999
        if 10 ** 9 <= n < 10 ** 12 :
            return n - 999999999 + n - 999999 + n - 999
        if 10 ** 12 <= n < 10 ** 15 :
            return  n - 999999999999 + n - 999999999 + n - 999999 + n - 999
        if 10 ** 15 <= n < 10 ** 16 :
            return n - 999999999999999 +  n - 999999999999 + n - 999999999 + n - 999999 + n - 999
