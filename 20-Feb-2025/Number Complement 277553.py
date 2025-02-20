# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        binary = deque()
        while num > 0:
            x = num % 2
            binary.appendleft(1 if x == 0 else 0 )
            num //= 2
        ans, exp = 0, 0
        while len(binary) > 0 :
            x = binary.pop()
            ans += x * (2 ** exp)
            exp += 1

        return ans