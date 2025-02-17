# Problem: B - Card Game - https://codeforces.com/gym/588094/problem/B

from collections import defaultdict
from collections import deque

n = int(input())
a = list(map(int,input().split()))
b = defaultdict(deque)
for i in range(n) :
    b[a[i]].appendleft(i+1)
a.sort()
i, j =0, n-1
while(i<j) :
    print(f"{b[a[i]].pop()} {b[a[j]].pop()}")
    i+=1
    j-=1

