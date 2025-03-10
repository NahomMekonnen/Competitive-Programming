# Problem: C - Robin’s Water Wisdom: Stop the Leaks! - https://codeforces.com/gym/594356/problem/C

n, A, B = map(int,input().split())
s = list(map(int,input().split()))
S, ans = sum(s), 0
firstHole = s[0]
s = s[1:]
s.sort(reverse=True)
i = 0
while ((firstHole/S)*A) < B and (i < len(s)):
    S -= s[i]
    ans += 1
    i+=1
print(ans)