class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        seen, ans = [], []
        k, i = 0, 0
        
        while i < len(nums):
            if nums[i] > 0 :
                seen.append(nums[i])
                i += 1
            else :
                while i < len(nums) and nums[i] < 0 :
                    i += 1
                    k += 1
                    if k > len(seen) :
                        ans.append(-1)
                    else :
                        ans.append(seen[-k])
                k = 0
            

        return ans
        
