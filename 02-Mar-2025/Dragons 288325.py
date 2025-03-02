# Problem: Dragons - https://codeforces.com/problemset/problem/230/A

from collections import defaultdict

s, n = map(int,input().split())
dragons, total = defaultdict(list), 0

for i in range(1,n+1) :
    dragons[i] = list(map(int,input().split()))
    total += i

d = sorted(dragons.items(), key=lambda item:item[1][0])

for key, drag in d: 
    if s <= drag[0] :
        break
    s += drag[1]
    total -= key

print("NO" if total else "YES")