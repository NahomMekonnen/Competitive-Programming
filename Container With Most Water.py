class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        area = 0
        while l < r :
            width = ( r - l )
            length = 0
            if height[l] < height[r] :
                length = height[l]
                l += 1
            else :
                length = height[r]
                r -= 1
            area = max(area, length * width)
        return area
