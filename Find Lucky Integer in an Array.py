class Solution:
    def findLucky(self, arr: List[int]) -> int:
        a = Counter(arr)
        for i in sorted(a, reverse = True) : 
            if i == a[i] : 
                return i
        return -1
