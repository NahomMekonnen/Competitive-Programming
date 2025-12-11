class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()
        for i in range(len(nums) - 1) :
            x = nums[i]
            while x != nums[i + 1] - 1:
                x += 1
                ans.append(x)
        return ans
