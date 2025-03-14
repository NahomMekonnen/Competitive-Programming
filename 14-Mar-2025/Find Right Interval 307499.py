# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for i in range(len(intervals)) :
            intervals[i].append(i)
        search = sorted(intervals)
        ans = []
        for i in range(len(intervals)) :
            s = intervals[i][1] 
            l, r = 0, len(intervals) -1
            last = None
            while l <= r :
                mid = ((l+r)//2) 
                if search[mid][0] >= s :
                    last = mid
                    r = mid -1
                elif search[mid][0] < s:
                    l = mid + 1

            if last == None :
                ans.append(-1)
            else :
                ans.append(search[last][2])
        return ans
 
        