class Solution:
    def countAsterisks(self, s: str) -> int:
        words = s.split("|")
        word = ""
        for i in range(0, len(words), 2) :
            word += words[i]
        cnt = Counter(word)
        return cnt["*"]
