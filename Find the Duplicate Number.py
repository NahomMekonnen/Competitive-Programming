class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        cnt = [0] * (len(nums) + 1)
        for i in nums :
            if cnt[i] :
                return i
            cnt[i] = i
        
