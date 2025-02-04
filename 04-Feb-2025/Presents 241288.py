# Problem: Presents - https://codeforces.com/problemset/problem/136/A

n = int(input())
friends  = list(map(int,input().split()))
ans = [0] * len(friends)
for i in range(len(friends)):
    ans[i] = friends.index(i+1) + 1
print(" ".join(list(map(str,ans))))