# Problem: Presents - https://codeforces.com/problemset/problem/136/A

n = int(input())
friends  = list(map(int,input().split()))
ans = [friends.index(i+1) + 1 for i in range(len(friends))]
print(" ".join(list(map(str,ans))))
