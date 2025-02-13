# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        map, ans = [0] * len(nums), []
        for i in nums:
            map[i] += 1
            if map[i] == 2:
                ans.append(i)
        return ans