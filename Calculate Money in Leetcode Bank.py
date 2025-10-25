class Solution:
    def totalMoney(self, n: int) -> int:
        if n <= 7 :
            return ( n * ( n + 1 ) ) // 2
        x , y = n // 7, n % 7
        j , ans = 0, 0
        for _ in range(x) :
            ans += ( ( 7 + j ) * ( 7 + j + 1 ) ) // 2  - ( (  j ) * (  j + 1 ) ) // 2
            j += 1
        ans +=  ( ( y + j ) * ( y + j + 1 ) ) // 2 -  ( (  j ) * (  j + 1 ) ) // 2
        return ans
