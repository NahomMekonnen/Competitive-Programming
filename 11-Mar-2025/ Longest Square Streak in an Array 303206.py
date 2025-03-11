# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        nums = set(nums)
        ans = -1
        check = defaultdict(int)
        for i in nums :
            check[i] += 1
        for i in nums :
            count = 0
            x = i
            while(check[x**2]) :
                count += 1
                x = x**2
            if count > 0 :
                count += 1
            ans = max(ans,count)
        return -1 if ans == 0 else ans
