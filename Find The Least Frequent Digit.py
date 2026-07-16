class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        cnt = defaultdict(int)
        while n > 0 :
            cnt[n % 10] += 1
            n //= 10

        cnt2 = defaultdict(list)
        for i in cnt :
            cnt2[cnt[i]].append(i)
        return min(cnt2[min(cnt2.keys())])
