# Problem: Maximum-sum-of-distinct-subarrays-with-length-k - https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        # so this is to check the previous occurence of an element
        # the previous index it occured at
        prevIdx = {}
        currSum = 0
        
        l=0
        for r in range(len(nums)):
            currSum += nums[r]
            # this retrieves the index and if it doesn't exist it'll be -1
            i = prevIdx.get(nums[r],-1)
            # updates the index
            prevIdx[nums[r]] = r
            
            # moves left pointer to the index and reducing the window
            # also checks if the window is bigger than k if so move left pointer one step
            while l <= i or r - l + 1 > k:
                currSum -= nums[l]
                l +=1

            # if the window is valid update the sum
            if r - l + 1 == k:
                res = max(res,currSum)
        return res