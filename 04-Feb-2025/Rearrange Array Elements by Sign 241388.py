# Problem: Rearrange Array Elements by Sign - https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        even , odd = 0 , 1
        for i in nums:
            if i > 0:
                ans[even] = i
                even += 2
            else:
                ans[odd] = i
                odd += 2
        return ans