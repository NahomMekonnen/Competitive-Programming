class Solution:
    def checkString(self, s: str) -> bool:
        for i in range(len(s) - 1, -1, -1) :
            if s[i] == 'a' :
                for j in range(i - 1, -1, -1) :
                    if s[j] == 'b' :
                        return False
                break
        return True