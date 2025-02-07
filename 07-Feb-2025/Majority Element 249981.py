# Problem: Majority Element - https://leetcode.com/problems/majority-element/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = Counter(nums)
        maxElement , maxCount = 0 , 0
        for i in elements.keys():
            maxCount = max(maxCount,elements[i])
            maxElement = i if maxCount == elements[i] else maxElement
        return maxElement