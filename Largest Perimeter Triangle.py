class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-2,0,-1) :
            x, y = nums[i+1], nums[i]
            for j in range(i-1,-1,-1) :
                if x + y > nums[j] and x + nums[j] > y and y + nums[j] > x :
                    return nums[j] + x + y
        return 0
