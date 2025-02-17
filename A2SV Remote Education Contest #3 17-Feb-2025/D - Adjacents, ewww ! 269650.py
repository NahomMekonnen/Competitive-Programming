# Problem: D - Adjacents, ewww ! - https://codeforces.com/gym/588094/problem/D

for _ in range(int(input())) :
    n = int(input())
    limit = n **2
    if n == 1: 
        print(1)
    elif n == 2 :
        print(-1)
    else:
        nums = []
        for i in range(1,limit + 1) :
            if i % 2 == 1:
                nums.append(i)
        for i in range(1,limit + 1) :
            if i % 2 == 0:
                nums.append(i)
        j = 0
        for i in range(n) :
            print(" ".join(map(str,nums[j:j+n])))
            j += n