class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ans = 0
        for i in range(len(arr1)) :
            distance = False
            for j in range(len(arr2)) :
                if abs(arr1[i]  - arr2[j]) <= d :
                    distance = True
                    break
            if not distance :
                ans += 1
        return ans
