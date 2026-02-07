class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        newNums, x = [0] * len(nums), 0
        for i in range(len(nums)-1) :
            if nums[i] > nums[i+1] :
                x = i + 1
        for i in range(len(nums)) :
            newNums[i] = nums[(i+x)%len(nums)]
        if newNums == nums == sorted(nums) :
            return  0
        if newNums == sorted(nums) :
            return len(nums) - x
        return -1
