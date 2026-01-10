
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans =  r

        while l <= r :
            mid = l + ( r - l ) // 2

            totalTime = 0
            for i in piles :
                totalTime += math.ceil(float(i)/mid)
            
            if totalTime <= h :
                ans = mid 
                r = mid - 1
            else :
                l = mid + 1
        return ans
