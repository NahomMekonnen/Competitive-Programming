# Problem: Reduction Operations to Make the Array Elements Equal - LeetCode - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/description/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        min_, op, count = nums[0], 0, 0
        for i in nums:
            if i != min_ :
                count += 1
                min_ = i
            op += count
        return op
