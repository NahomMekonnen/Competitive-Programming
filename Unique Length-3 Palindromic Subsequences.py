class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = Counter(s)

        for m in s:
            right[m]-=1

            for i in left:
                if right[i] > 0:
                    res.add((m,i))
            
            left.add(m)

        
        return len(res)
