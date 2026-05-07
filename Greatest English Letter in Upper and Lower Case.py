class Solution:
    def greatestLetter(self, s: str) -> str:
        s = sorted(list(s), reverse = True)
        for i in s :
            if i.isupper() :
                break
            if i.upper() in s :
                return i.upper()  
        return ""
