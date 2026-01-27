# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

t  = int(input())
base = "codeforces"
for i in range(t):
    word = input()
    count = 0
    for i in range(10):
        if word[i] != base[i]:
            count += 1

    print(count)
