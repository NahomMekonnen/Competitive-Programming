class Solution:
    def numSub(self, s: str) -> int:
        m = s.split("0")
        ans = 0
        for i in m :
            if i.isdigit() :
                n = len(i)
                ans += ((n + 1) * n) // 2
        return  ans % ((10 ** 9) + 7)
