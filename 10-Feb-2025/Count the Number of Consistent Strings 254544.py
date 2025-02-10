# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans= 0
        for word in words:
            cant = False
            for i in word:
                if i not in allowed:
                    cant = True
                    break
            if not cant:
                ans += 1
        return ans
            