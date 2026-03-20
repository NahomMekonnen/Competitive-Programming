class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        keys = "".join(s.split("-")).upper()
        ans = ""
        n = len(keys)
        if n % k != 0 :
            ans += keys[:n%k] 
        for i in range(n%k,len(keys),k) :
            add = "" if i == 0 else "-"
            ans += add + keys[i:i+k]
        return ans
