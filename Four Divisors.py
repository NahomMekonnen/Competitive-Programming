class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        nums = set(nums)
        ans = 0
        for num in nums :
            n, x = 0, 0
            visit = set()
            for i in range(1,int(num**0.5) + 1) :
                if i in visit: 
                    break
                if num % i == 0 :
                    n += 1
                    visit.add(i)
                    visit.add(num//i)
                if len(visit) > 4 : 
                    break
            if len(visit) == 4 :
                ans += sum(visit) * cnt[num]
        return ans
