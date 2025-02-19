# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def sumDigits(self, n: int) -> int:
        ans = 0
        while n > 0 :
            ans += (n%10) ** 2
            n //=10
        return ans

    def isHappy(self, n: int) -> bool:
        check = set()
        while True :
            num = self.sumDigits(n)
            if num in check :
                return False
            check.add(num)
            if num == 1 :
                break
            n = num
        return True