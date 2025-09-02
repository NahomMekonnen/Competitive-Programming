class Solution:
    def maximum69Number (self, num: int) -> int:
        n = int(str(num)[::-1])
        ans, one, p = 0, True, 1
        while n > 0 :
            digit = n % 10 
            n//= 10
            if one and digit == 6:
                digit = 9   
                one = False
            ans += p * digit
            p *= 10
        ans = int(str(ans)[::-1])
        return ans 
            
