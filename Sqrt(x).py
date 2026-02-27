class Solution:
    def mySqrt(self, x: int) -> int:
        if (x == 0 or x == 1) :
            return x

        start ,end = 1, x

        while (start <= end) :
            mid = start + (end - start)// 2

            if (mid == x // mid) :
                return mid
            elif (mid < x // mid) :
                start = mid + 1
            else :
                end = mid - 1

        return end
