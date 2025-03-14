# Problem: Count Pairs Whose Sum is Less than Target - https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans, l, r = 0, 0, len(nums) - 1
        while l < r:
            s = nums[l] + nums[r]
            if s >= target :
                r -= 1
            else :
                ans += (r - l)
                l += 1
        return ans