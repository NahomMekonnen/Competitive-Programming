class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i in range(len(s)) :
            idx = ord(s[i]) - ord('a') + 1
            idx = 26 - idx + 1
            ans += (idx * (i + 1))
        return ans