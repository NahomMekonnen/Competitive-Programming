# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left , right = 0 , len(height) - 1
        maxArea = 0
        while left < right :
            area = 0
            if height[left] <= height[right] :
                area = (right - left) * (height[left])
                left += 1
            else :
                area = (right - left) * height[right]
                right -= 1
            maxArea = max(area,maxArea)
        return maxArea
            