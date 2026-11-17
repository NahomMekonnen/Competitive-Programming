class Solution:
    def countEven(self, num: int) -> int:
        def checker(self, n: int) -> bool :
            total = 0
            while n :
                total += n % 10
                n //= 10 
            return total % 2 == 0
        ans = 0 
        for i in range(1, num + 1) :
            if checker(self, i) :
                ans += 1
        return ans