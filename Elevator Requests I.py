class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        curr, ans = 0, 0
        for i in requests :
            ans += abs(curr - i)
            curr = i
        return ans