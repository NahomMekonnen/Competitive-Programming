class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
       
        n1, n2 = len(name), len(typed)
        p1, p2 = 0, 0
        while p1 < n1 and p2 < n2 :

            if p1 == p2 == 0 and name[p1] != typed[p2] :
                return False
            cnt1, cnt2 = defaultdict(int), defaultdict(int)
            if name[p1] == typed[p2] :
                while p1 + 1 < n1 and name[p1] == name[p1 + 1] :
                    cnt1[name[p1]] += 1
                    p1 += 1
                while p2 + 1 < n2 and typed[p2] == typed[p2 + 1] :
                    cnt2[typed[p2]] += 1
                    p2 += 1
                if cnt1[name[p1]] > cnt2[typed[p2]] :
                    return False
                p1 += 1
                p2 += 1
            else :
                return False
        
        if p2 < n2 or p1 < n1 :
            return False
        return True
