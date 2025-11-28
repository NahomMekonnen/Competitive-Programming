class Solution:
    def sumOfDigits(self, n: int) -> int :
        s = 0
        while n :
            s += n % 10
            n //= 10 
        return s

    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = defaultdict(int)
        ans = 0
        for i in range(lowLimit, highLimit + 1) :
            s = self.sumOfDigits(i)
            boxes[s] += 1
            ans = max(boxes[s], ans)
        return ans
