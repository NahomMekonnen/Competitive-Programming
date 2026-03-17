class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        bit = ""
        while n > 0 :
            bit += str(n%2)
            n //= 2
        ans = [0, 0]
        for i in range(len(bit)) :
            if bit[i] == "1" :
                if i % 2  == 0 :
                    ans[0] += 1
                else :
                    ans[1] += 1
        return ans
