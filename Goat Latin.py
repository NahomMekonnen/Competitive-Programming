class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel = "aeiouAEIOU"
        add = "a"
        words = sentence.split()
        for i in range(len(words)) :
            if words[i][0] not in vowel :
                words[i] += words[i][0]
                words[i] = words[i][1:]
            words[i] += "ma" + add
            add += "a"
       return (" ").join(words).strip()
