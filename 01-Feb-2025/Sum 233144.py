# Problem: Sum - https://codeforces.com/contest/1742/problem/A

t = int(input())
for i in range(t):
    arr = list(map(int,input().split()))
    arr = sorted(arr)
    print("YES" if( (arr[0] + arr[1]) == arr[2]) else "NO")