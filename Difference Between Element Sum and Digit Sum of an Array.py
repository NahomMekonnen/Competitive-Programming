class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0
        def digitSum(num: int) -> int:
            total = 0
            while num > 0 :
                total += num % 10 
                num //= 10 
            return total
        
        for i in nums :
            digit_sum += digitSum(i)
        return abs(element_sum - digit_sum)
