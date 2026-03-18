class Solution:
    def residuePrefixes(self, s: str) -> int:
        ans = 0
        for i in range(1, len(s)+1) :
            prefix = s[:i]
            if len(prefix) % 3 == len(set(prefix)) :
                ans +=1
        return ans
