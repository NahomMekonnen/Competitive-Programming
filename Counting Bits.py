class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)
        def count(self, x: int) -> int :
            cnt = 0
            while x > 0 :
                pop = x % 2
                if pop == 1 :
                    cnt += 1 
                x //= 2
                
            return cnt
            
        for i in range(0, n + 1) :
            ans[i] = count(self, i)
            
        return ans 
           
           
           
       