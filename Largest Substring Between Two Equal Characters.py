class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans, pos = -1, defaultdict(int)
        for i in range(len(s)) :
            if pos[s[i]] :
                ans = max(ans,(i)-pos[s[i]])
            else :
                pos[s[i]] = (i+1)
        return ans
