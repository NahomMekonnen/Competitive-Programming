class Solution:
    def averageValue(self, nums: List[int]) -> int:
        n = [i for i in nums if i % 2 == 0 and i % 3 == 0]
        return sum(n)//len(n) if n else 0
