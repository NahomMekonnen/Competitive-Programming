class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, suf = [0] * len(nums), [0] * len(nums)
        pre[0], suf[-1] = nums[0], nums[-1]
        for i in range(1,len(nums)) :
            pre[i] = pre[i-1] * nums[i]
        for i in range(len(nums)-2,-1,-1) :
            suf[i] = suf[i+1] * nums[i]
        ans = []
        for i in range(len(nums)) :
            if i == 0 :
                ans.append(suf[i+1])
            elif i == len(nums) - 1:
                ans.append(pre[i-1])
            else :
                ans.append(pre[i-1] * suf[i+1])
        return ans
