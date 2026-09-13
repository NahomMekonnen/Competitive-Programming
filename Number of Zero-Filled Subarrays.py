class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        l, ans = 0, 0
        while l < len(nums) : 
            r = l
            if nums[r] == 0 :
                while r < len(nums) and nums[r] == 0 :
                    r += 1
                s = r - l
                ans += (s * (s + 1))//2
            l = r + 1
        return ans
