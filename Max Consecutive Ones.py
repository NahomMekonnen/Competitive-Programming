class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append(0)
        last = -1
        ans = 0
        for i in range(len(nums)) :
            if nums[i] == 0 :
                ans = max(ans, i - last - 1)
                last = i
        if last == -1 :
            return len(nums)
        return ans
