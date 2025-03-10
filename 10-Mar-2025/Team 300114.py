# Problem: Team - https://codeforces.com/contest/231/problem/A

ans = 0
for _ in range(int(input())) :
    if sum(map(int,input().split())) >= 2:
        ans += 1
print(ans)
