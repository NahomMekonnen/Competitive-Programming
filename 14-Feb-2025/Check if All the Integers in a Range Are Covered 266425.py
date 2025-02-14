# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        p = [0] * 51
        for i in ranges :
            for j in range(i[0],(i[1] + 1)):
                p[j] += 1
        for i in range(left, right + 1) :
            if p[i] == 0:
                return False
        return True