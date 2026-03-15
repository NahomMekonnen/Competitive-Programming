class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        c = Counter("".join(words))
        print(c)
        for i in c :
            if c[i] % len(words) != 0 :
                return False
        return True
