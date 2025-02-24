# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

from collections import defaultdict


for _ in range(int(input())):
    n  = int(input())
    a = list(map(int,input().split()))
    hashmap = defaultdict(int)
    cnt = 0 
    for i in range(n) :
        x = (a[i] - i)
        cnt += hashmap[x]
        hashmap[x] += 1   
    print(cnt)