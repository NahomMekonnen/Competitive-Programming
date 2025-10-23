class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2 :
            newS = ""
            for i in range(len(s)-1) :
                newS += str((int(s[i]) + int(s[i+1])) % 10)
            s = newS
        return s[0] == s[1]
