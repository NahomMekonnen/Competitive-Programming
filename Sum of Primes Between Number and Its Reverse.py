class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r = int(str(n)[::-1])
        ans = 0

        for i in range (min(n, r), max(n, r) + 1) :   
            if i == 2 :
                ans += i
            elif i > 2 and i % 2 != 0 :
                root = int(sqrt(i))
                has_factors = False
                for f in range(3, root + 1, 2) :
                    if i % f == 0 :
                        has_factors = True
                        break
                if not has_factors :
                    ans += i           

        return ans
