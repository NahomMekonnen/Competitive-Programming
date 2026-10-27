class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        def countPrimes(n: int) -> int :
            prime = [True] * (n + 1)
            p = 2
            while p * p <= n:
                if prime[p]:
                    for i in range(p * p, n + 1, p):
                        prime[i] = False
                p += 1
            res = 0
            for p in range(2, n + 1):
                if prime[p]:
                    res += 1
            return res
        
        cntP = countPrimes(n)

        return (factorial(cntP) * factorial(n - cntP)) % ((10 ** 9)+ 7)
        
