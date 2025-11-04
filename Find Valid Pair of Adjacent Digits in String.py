class Solution:
    def findValidPair(self, s: str) -> str:
        mp = Counter(list(s))
        for i in range(1,len(s)) :
            if int(s[i-1]) == mp[s[i-1]] and int(s[i]) == mp[s[i]] and s[i-1] != s[i] :
                return s[i-1:i+1]
        return ""
