class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        start = floor(sum(nums)/len(nums)) + 1 
        start = 1 if start < 1 else start
        while cnt[start] :
            start += 1
        return start