# Problem: C - Sura loves coding - https://codeforces.com/gym/586622/problem/C

n = int(input())
s = input()
left, middle,right= [],s[0],''
for i in range(1,n) :
    if i % 2 ==0 :
        right += s[i]
    else :
        left.append(s[i])
left.reverse()
left = "".join(left)
ans = list( left+middle + right)
if n % 2 ==0:
    ans.reverse()
print("".join(ans))