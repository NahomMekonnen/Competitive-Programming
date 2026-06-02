class Solution:
    def earliestFinishTime(self, lst: List[int], ld: List[int], wst: List[int], wd: List[int]) -> int:
        ans = float('Inf')

        for i in range(len(lst)):
            lf = lst[i] + ld[i]
            for j in range(len(wst)) :
                ans = min(ans, max(lf, wst[j]) + wd[j])

        for i in range(len(wst)):
            wf = wst[i] + wd[i]
            for j in range(len(lst)) :
                ans = min(ans, max(wf, lst[j]) + ld[j])
        return ans
