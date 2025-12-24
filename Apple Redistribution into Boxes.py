class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)
        n = sum(apple)
        ans = 0
        for i in capacity :
            n -= i
            ans += 1
            if n <= 0 :
                break
        return ans
