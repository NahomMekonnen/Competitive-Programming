class Solution:
    def rotatedDigits(self, n: int) -> int:
        def rot(num: int) -> int :
            if num == 0 or num == 1 or num == 8 :
                return num
            if num == 2 :
                return 5
            if num == 5 :
                return 2 
            if num == 6 :
                return 9
            if num == 9 :
                return 6
            return -1

        ans = 0
        for i in range(1, n +  1) :
            x = i 
            cnt = 0
            valid = True
            while x > 0 :
                d = x % 10 
                r = rot(d) 
                if r == -1 :
                    valid = False
                if r != d :
                    cnt += 1
                x //= 10
            if cnt == 0 :
                valid = False
            if valid :
                ans += 1
        return ans
