# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

array = [
    list(map(int,input().split())),
    list(map(int,input().split())),
    list(map(int,input().split())),
    list(map(int,input().split())),
    list(map(int,input().split()))
]
indices = []
for i in range(len(array)) :
    for j in range(len(array)) :
        if array[i][j] == 1:
            indices = [i,j]
            break
print(abs(indices[0]-2)+abs(indices[1]-2))
