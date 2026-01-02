class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        for i in nums :
            if cnt[i] :
                return i
            cnt[i] += 1
