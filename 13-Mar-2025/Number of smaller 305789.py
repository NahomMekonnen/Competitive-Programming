# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n, m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
l, ans = 0, []
for i in range(len(b)) :
    
    while l < len(a) and a[l] < b[i] :
        l += 1
    ans.append(l)
print(*ans)
