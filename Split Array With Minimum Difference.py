class Solution:
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)
        inc, dec = [False] * n, [False] * n
        inc[0] = dec[-1] = True
        for i in range(1, n) :
            if nums[i] <= nums[i - 1] :
                inc[i] = False
                break
            else :
                inc[i] = True
            
        for i in range(n-2, -1, -1) :
            if nums[i] <= nums[i + 1] :
                dec[i] = False
                break 
            else :
                dec[i] = True
        
        absDiff, exists = float('inf'), False
        for i in range(n - 1) :
            if inc[i] and dec[i + 1] :
                exists = True 
                absDiff = min( absDiff , abs( sum( nums[ :i + 1] ) - sum( nums[i + 1:] ) ) )

        if exists :
            return absDiff
        return -1