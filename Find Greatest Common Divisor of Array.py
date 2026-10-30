class Solution:
    def findGCD(self, nums: list[int]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        return gcd(max(nums), min(nums))