# Problem: Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r :
            x = numbers[l] + numbers[r]
            if x < target :
                l += 1
            elif x > target :
                r -= 1
            else :
                return [l+1,r+1]
        return []