class Solution:
    def maxPower(self, s: str) -> int:
        power = []
        for i in range(len(s)) :
            j = i + 1
            while j < len(s) and s[j] == s[i] :
                j += 1
            power.append(j-i)
        return max(power)
