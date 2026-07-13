
class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n < 1000 :
            return str(n)
        ans = []
        while n > 0 :
            k = str(n % 1000)
            n //= 1000
            if n > 0 :
                k = "00" + k
                k = k[-3:]
            ans.append(k)
        
        return ".".join(ans[::-1])
