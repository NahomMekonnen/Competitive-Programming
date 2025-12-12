class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mindiff = float("inf")
        for i in range(1, len(arr)) :
            diff = abs(arr[i] - arr[i-1])
            mindiff = min(diff,mindiff)
        ans = []
        for i in range(1, len(arr)) :
            diff = abs(arr[i] - arr[i-1])
            if diff == mindiff :
                ans.append([arr[i-1],arr[i]]) 
        return ans
