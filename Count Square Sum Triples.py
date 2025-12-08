class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for a in range(1,n + 1) :
            for b in range( a + 1,n + 1) :
                root = sqrt((a ** 2) + ( b ** 2))
                if root == float(int(root)) and root <= n :
                    ans += 2
        return ans
