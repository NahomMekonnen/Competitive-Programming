# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

from collections import Counter
n, k = map(int,input().split())

a = sorted(list(map(int,input().split())))
ans = a[0]-1 if k == 0 else a[k-1]
cnt = 0 
for i in a :
    if i > ans :
        break
    cnt += 1

if ans < 1 or cnt != k :
    print(-1)
else :
    print(ans)

