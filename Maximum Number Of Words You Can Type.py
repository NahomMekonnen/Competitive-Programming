class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        ans = len(words)
        for word in words :
            for l in brokenLetters : 
                if l in word :
                    ans -= 1
                    break
        return ans
