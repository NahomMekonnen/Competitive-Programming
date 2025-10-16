class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        ans = [0] * len(temp)
        stk = []
        for i in range(len(temp)-1,-1,-1) :
            while stk and temp[stk[-1]] <= temp[i] :
                stk.pop()
            if stk :
                ans[i] = (stk[-1] - i)
            stk.append(i)
        return ans
