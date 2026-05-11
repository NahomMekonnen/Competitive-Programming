class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        cnt = 1
        for i in arr :
            if c[i] == 1 :
                if cnt == k :
                    return i
                cnt += 1
        return ""
