class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        cnt = Counter(nums)
        for i in nums :
            if i % 2 == 0 and cnt[i] == 1 :
                return i
        return -1
