# Problem: A - Nathan is rich - https://codeforces.com/gym/588094/problem/A

t = int(input())
for i in range(t) :
    n = int(input())
    ans = 0
    while n % 4 != 0:
        ans += 1
        n -= 2
    ans += n//4
    print(ans)