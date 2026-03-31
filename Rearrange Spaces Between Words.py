class Solution:
    def reorderSpaces(self, text: str) -> str:
        cnt = 0
        for i in text :
            if i == " " :
                cnt += 1
        words = text.split()
        size = len(words)
        ans = ""
        if size == 1 :
            return words[0] + (" " * cnt)
        for i in range(size) :
            ans += words[i]
            if i != size - 1 :
                ans += " " * (cnt//(size - 1))
        if cnt % (size-1) != 0 :
            ans += " " * (cnt % (size-1))
        return ans
