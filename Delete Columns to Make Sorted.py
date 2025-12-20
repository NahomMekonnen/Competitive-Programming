class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cols = defaultdict(list)
        for s in strs :
            for i in range(len(s)) :
                cols[i].append(s[i])
        ans = 0
        for i in range(len(s)) :
            if cols[i] != sorted(cols[i]) :
                ans += 1
        return ans
