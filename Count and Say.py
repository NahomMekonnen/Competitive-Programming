class Solution:
    def countAndSay(self, n: int) -> str:
        ans = ""
        for i in range(n) : 
            if i + 1 == 1 :
                ans = "1"
            else :
                ans = self.rLE(ans)

        return ans

    def rLE(self, s: str) -> str :
        n = len(s)
        l, r = 0, 1
        RLE = ""
        
        while l < n :

            while r < n and s[r] == s[l] :
                r += 1
            
            RLE += str(r - l) + s[l]
            l = r

        return RLE
            


