class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        d, score = set(divisors), 0
        divs = defaultdict(list)
        for i in d :
            div = 0
            for j in nums :
                if j % i == 0 :
                    div += 1
            divs[div].append(i)
        m = -float("inf")
        for i in divs :
            m = max(i,m)
        return min(divs[m])
