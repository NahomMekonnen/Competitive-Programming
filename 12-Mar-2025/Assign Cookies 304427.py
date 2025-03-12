# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j, count = 0, 0, 0
        while i < len(g) and j < len(s) :
            if g[i] <= s[j] :
                count += 1
                i += 1
            j += 1
        return count
