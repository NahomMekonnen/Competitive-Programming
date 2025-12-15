class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans , i = 0, 0
        while i < len(s) :
            cnt = defaultdict(int)
            for j in range(i,len(s)) :
                cnt[s[j]] += 1
                if cnt["R"] == cnt["L"] :
                    ans += 1
                    i = j + 1
                    break
        return ans
