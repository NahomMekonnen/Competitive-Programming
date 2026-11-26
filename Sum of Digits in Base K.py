class Solution:
    def sumBase(self, n: int, k: int) -> int:
        baseK = []
        while n > 0 :
            baseK.append(n % k)
            n //= k
        
        return sum(baseK)

