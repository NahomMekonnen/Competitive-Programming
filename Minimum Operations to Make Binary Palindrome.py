class Solution:
    def minOperations(self, nums: List[int]) -> List[int]:
        p = [0] * 5001  

        for i in range(1, len(p)) :
            b = f"{i:b}"
            if b == b[::-1] :
                p[i] += 1
            
        ans = [0] * len(nums)

        for i in range(len(nums)) :
            n = nums[i]
            if p[n] != 1 :
                l, r = n, n 

                while l > -1 and p[l] != 1 :
                    l -= 1
                while r < 5001 and p[r] != 1 :
                    r += 1
                
                if l > -1 and p[l] == 1 :
                    ans[i] = n - l
                if r < 5001 and p[r] == 1 :
                    ans[i] = min(ans[i], r - n)
                

                        
                    
        return ans
