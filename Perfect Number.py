class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1 :
            return False
        divisors = 0
        for i in range(1,(int(sqrt(num))) + 1) :
            if num % i == 0 :
                if num % i == i :
                    divisors += i
                else :
                    divisors += i
                    divisors += (num // i)
        divisors -= num
        return divisors == num 
