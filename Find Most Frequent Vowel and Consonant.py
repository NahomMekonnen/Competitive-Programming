class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = defaultdict(int)
        consonants = defaultdict(int)
        maxC, maxV = 0, 0
        for i in s :
            if i in "aeiou" :
                vowel[i] += 1
                maxV = max(vowel[i],maxV)
            else :
                consonants[i] += 1
                maxC = max(consonants[i],maxC)
        return maxC + maxV
