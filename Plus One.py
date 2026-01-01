class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num, exp = 0, 1
        for i in range(len(digits) - 1, -1, -1) :
            num += digits[i] * exp
            exp *= 10
        num += 1
        ans = []
        while num :
            ans.append(num%10)
            num//=10
        return ans[::-1]
