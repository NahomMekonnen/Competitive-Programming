class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = float("inf")

        for size in range(l, r + 1) :
        
            for i in range(n - size + 1) :
                currSum = 0
                for j in range(size) :
                    currSum += nums[i + j]
                if currSum > 0 :
                    ans = min(currSum, ans)


        return -1 if ans == float("inf") else ans