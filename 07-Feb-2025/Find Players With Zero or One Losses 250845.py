# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win, loss= dict(), dict()
        for i in matches:
            win[i[0]] = win.get(i[0],0) + 1
            loss[i[1]] = loss.get(i[1],0) + 1
        ans,w,l = [], [] ,[]
        for i in win:
            if loss.get(i,0) == 0:
                w.append(i)
        w.sort()
        for i in loss:
            if loss[i] == 1:
                l.append(i)
        l.sort()
        ans.append(w)
        ans.append(l)
        return ans