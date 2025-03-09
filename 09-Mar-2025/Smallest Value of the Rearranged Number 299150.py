# Problem: Smallest Value of the Rearranged Number - https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0 :
            return  0

        sign = 1 if num > 0 else -1
        num = abs(num)
        d = [] # digits
        while num > 0 :
            d.append(num%10)
            num//= 10
        d.sort()
        ans = 0
        if sign == -1 :
            for i in range(len(d)-1,-1,-1) :
                ans += d[i]
                if i == 0 :
                    break
                ans *= 10
            ans *= sign
        else :
            j = 0
            while d[j] == 0 :
                j += 1
            d[0], d[j] = d[j], d[0]

            for i in range(len(d)) :
                ans += d[i]
                if i == len(d) - 1 :
                    break
                ans *= 10
        return ans
