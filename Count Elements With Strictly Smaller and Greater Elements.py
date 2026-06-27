class Solution:
    def countElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        nums = sorted(list(set(nums)))
        ans = 0
        for i in range(1,len(nums) - 1) :
            ans += cnt[nums[i]]
        return ans
