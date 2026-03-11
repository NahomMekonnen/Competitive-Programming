class Solution:
    def largestEven(self, s: str) -> str:
        while s != "" :
            if int(s) % 2 == 0 :
                return s
            s = s[:-1]
        return s
