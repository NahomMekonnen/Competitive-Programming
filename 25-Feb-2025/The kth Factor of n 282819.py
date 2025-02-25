# Problem: The kth Factor of n - https://leetcode.com/problems/the-kth-factor-of-n/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors =  []
        f = n
        while f > 0 :
            if (n % f) == 0 :
                factors.append(f)
            f -= 1
        factors.sort()
        return factors[k-1] if k <= len(factors) else -1

            