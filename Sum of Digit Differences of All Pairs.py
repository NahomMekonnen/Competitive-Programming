class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        freq = defaultdict(lambda: [0] * 10)
        digits = len(str(nums[0]))

        for i in nums :
            x, p = i, 0 
            while x > 0 :
                freq[p][x % 10] += 1
                x //= 10
                p += 1
        ans = 0     
        n = len(nums)
        for i in freq :
            for j in freq[i] :
                ans += j * (n - j)
        return ans // 2
        
