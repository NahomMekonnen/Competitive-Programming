class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        forward = True
        ans = 0
        while(k > 0) :
            if forward :
                ans += 1
                if (ans == n) :
                    ans -= 2
                    forward = False
            else :
                ans -= 1
                if (ans == -1) :
                    ans += 2
                    forward = True
            k-=1

        return ans
