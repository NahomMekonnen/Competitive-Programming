class Solution:
    def hIndex(self, c: List[int]) -> int:
        cnt = defaultdict(int)
        c.sort(reverse = True)
        h = 0
        for i in range(len(c)) : 
            gtoe = i + 1 # greater than or equal count
            cnt[c[i]] = gtoe
        for i in cnt :
            if i != 0 :
                if i <= cnt[i] :
                    h = max(h, i)
                else :
                    h = max(h, cnt[i])
        return  h
