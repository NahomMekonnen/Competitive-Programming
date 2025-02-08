# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt, num = 0 , x^y
        while num > 0:
            if num % 2 == 1:
                cnt +=1
            num //= 2
        return cnt