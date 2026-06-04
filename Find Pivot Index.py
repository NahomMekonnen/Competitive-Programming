class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pre, post = [0] * n, [0] * n
        pre[0], post[-1] = nums[0], nums[-1]

        for i in range(1, n) :
            pre[i] = nums[i] + pre[i-1]

        for i in range(n-2,-1,-1) :
            post[i] = nums[i] + post[i + 1]

        for i in range(n) :
            if pre[i] == post[i] :
                return i
                
        return -1
