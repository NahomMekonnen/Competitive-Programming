class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        n = len(nums)
        total = [0] * ((n * (n + 1))//2 )
        idx = 0
        for i in range(n) :
            totalSum = 0
            for j in nums[i:]:
                totalSum += j 
                total[idx] = totalSum 
                idx += 1
        total.sort()
        # print(total)
        return sum(total[left-1:right]) % ((10 ** 9) + 7)