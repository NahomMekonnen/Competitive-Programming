class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        pre, suf = [0] * len(nums), [0] * (len(nums) + 1)
        ans = []
        check = set()
        for i in range(len(nums)) :
            check.add(nums[i])
            pre[i] = len(check)
        check = set()
        for i in range(len(nums)-1,-1,-1) :
            check.add(nums[i])
            suf[i] = len(check)
        for i in range(len(nums)) :
            ans.append(pre[i]-suf[i + 1])
        return ans
