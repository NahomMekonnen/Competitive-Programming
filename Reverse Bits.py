class Solution:
    def reverseBits(self, n: int) -> int:
        ans = ""
        while n > 0 :
            ans += str(n%2)
            n //= 2
        if len(ans) < 32 :
            ans += "0" * (32 - len(ans))
        return int(ans,2)
