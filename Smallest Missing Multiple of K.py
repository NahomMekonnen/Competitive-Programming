class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)) :
            num = k * (i + 1)
            if num not in nums :
                return num
        return k * (len(nums) + 1)
