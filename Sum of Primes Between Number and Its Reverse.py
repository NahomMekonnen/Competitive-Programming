class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r = int(str(n)[::-1])
        ans = 0
        for i in range (min(n, r), max(n, r) + 1) :      


            if i > 10 :
                if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % 11 != 0 :
                ans += i
            else if i == 2 or i == 3 or i == 5 or i == 7 :
                ans += i

        

        return ans