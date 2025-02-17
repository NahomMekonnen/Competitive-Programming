# Problem: D - Mugisho and Rufeyda - https://codeforces.com/gym/586622/problem/D

inputs = list(map(int,input().split()))
n , t = inputs[0], inputs[1]
limit = 10 **n 
found = False

for i in range(limit//10,limit):
    if (i % t) == 0 :
        print(i)
        found = True
        break
if not found:
    print(-1)

