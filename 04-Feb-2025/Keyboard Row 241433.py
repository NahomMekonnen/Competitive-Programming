# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1, row2, row3 = list("qwertyuiop"), list("asdfghjkl"),list("zxcvbnm")
        ans = []
        for word in words:
            w = list(word.lower())
            # print(w)
            rw1 , rw2, rw3 = 0 , 0, 0
            for i in w:
                if not i in row1:
                    rw1 +=1
                if not i in row2 :
                    rw2 += 1
                if not i in row3 :
                    rw3 += 1
            if min(rw1,min(rw2,rw3)) == 0:
                ans.append(word)
        return ans