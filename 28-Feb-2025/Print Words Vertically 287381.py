# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words, longest = s.split(), 0
        for i in words:
            longest = max(longest,len(i))
        ans = []
        for i in range(longest) :
            row = []
            for j in range(len(words)) :
                row.append(words[j][i] if i < len(words[j]) else " ")
            ans.append("".join(row).rstrip())
        return ans