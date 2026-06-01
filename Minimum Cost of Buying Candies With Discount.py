class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        ans = sum(cost)
        idx = 2
        for i in range(len(cost)) :
            if i == idx :
                ans -= cost[i]
                idx += 3
        return ans
