class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def isPrime(self, n: int) -> int :
            if n == 1 :
                return False
            for i in range(2,int(sqrt(n)) + 1) :
                if n % i == 0 :
                    return False
            return True
        ans = 0
        n = len(nums)
        for i in range(n) :
            if isPrime(self, nums[i][i]) :
                ans = max(ans, nums[i][i])
            if isPrime(self, nums[i][n - i - 1]) :
                ans = max(ans, nums[i][n - i - 1])
           
        return ans