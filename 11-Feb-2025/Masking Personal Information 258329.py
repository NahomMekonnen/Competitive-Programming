# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        masked = ""
        s = s.lower()
        if "." in s:
            idx = s.find("@")
            masked = s[0] + "*****" + s[idx-1:]
        else:
            number = [i for i in s if i.isdigit()]
            n = len(number)
            masked = "***-***-" + "".join(number[-4:])
            if n == 11:
                masked = "+*-"+masked
            elif n == 12:
                masked = "+**-"+masked
            elif n == 13:
                masked = "+***-"+masked



        return masked