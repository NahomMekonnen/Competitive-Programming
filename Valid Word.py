class Solution:
    def isValid(self, word: str) -> bool:
        vowels = "aeiouAEIOU"
        if len(word) < 3 :
            return False
        v, c = False, False
        for i in word :
            if i in string.punctuation :
                return False
            if i.isalpha() :
                if i in vowels :
                    v = True
                else :
                    c = True
        return c and v
