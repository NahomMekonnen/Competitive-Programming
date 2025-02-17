# Problem: B - The special paintbrush - https://codeforces.com/gym/586622/problem/B

t  = int(input())
for i in range(t):
    n = int(input())
    s = input()
    i, j =0, n-1
    while(s[i]!="B"):
        i += 1
    while(s[j]!="B"):
        j -= 1
    j+=1
    print(j-i)
        
