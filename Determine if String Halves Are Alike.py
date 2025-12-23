class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s1, s2 = s[:len(s)//2], s[len(s)//2:]
        cntV1, cntV2, cntC1, cntC2 = 0, 0, 0, 0
        for i in range(len(s1)) :
            if s1[i] in vowels :
                cntV1 += 1
            else :
                cntC1 += 1
            if s2[i] in vowels :
                cntV2 += 1
            else :
                cntC2 += 1
        return cntV1 == cntV2 and cntC1 == cntC2
