class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt( x: int) -> int :
            largest, size = 0, 0
            while x > 0 :
                largest = max(largest, x % 10)
                x //= 10
                size += 1
            return int(str(largest) * size)

        return sum([encrypt(i) for i in nums])
