class Solution:
    def scoreBalance(self, s: str) -> bool:
        arr = [ord(i) - ord('a') + 1 for i in s]
        n = len(s)
        pre, post = [0] * n, [0] * n
        pre[0], post[-1] = arr[0], arr[-1]
        for i in range(1, n) :
            pre[i] = pre[i - 1] + arr[i]
        for i in range(n- 2, -1, -1) :
            post[i] = post[i + 1] + arr[i]
        for i in range(n - 1) :
            if pre[i] == post[i + 1] :
                return True
        return False
