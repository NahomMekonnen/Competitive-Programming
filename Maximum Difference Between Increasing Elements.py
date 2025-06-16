class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        smallest, diff = sys.maxsize, -(sys.maxsize)-1
        mins = [smallest] * (len(nums) -1 )
        for i in range(len(nums) - 1) :
            smallest = min(smallest,nums[i])
            mins[i] = smallest
        for i in range(len(nums)-1,0,-1) :
            print(nums[i], mins[i-1])
            diff = max(nums[i]-mins[i-1],diff)
        return -1 if diff <= 0 else diff
