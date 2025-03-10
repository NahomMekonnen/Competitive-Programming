# Problem: B - Thousand Sunny's Network Setup - https://codeforces.com/gym/594356/problem/B

from collections import Counter

n, k = map(int,input().split())
a = list(map(int,input().split()))
count= Counter(a)
a = sorted(list(set(a)), reverse=True)
ans , curr  =0, 0
for i in range(len(a)):
    curr += count[a[i]]
    if curr >= k: 
        ans = a[i]
        break
print(ans)