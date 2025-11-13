class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        map = defaultdict(list)
        for i in range(len(nums)) :
            map[nums[i]].append(i)
        ans = float("inf")
        for m in map :
            if len(map[m]) < 3 :
                continue
            d = 0    
            for i in range(len(map[m])-2) :
                d = abs(map[m][i] - map[m][i + 1]) + abs(map[m][i] - map[m][i + 2]) + abs(map[m][i + 1] - map[m][i + 2])
                ans = min(ans,d)
        return ans if ans != float("inf") else -1
