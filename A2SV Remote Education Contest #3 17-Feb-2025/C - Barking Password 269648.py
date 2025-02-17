# Problem: C - Barking Password - https://codeforces.com/gym/588094/problem/C

pswrd = input()
found = False
first, second = [], []
for i in range(int(input())) :
    wrd = input()
    first.append(wrd[0])
    second.append(wrd[1])
    if wrd == pswrd :
        found = True
for s in second :
    for f in first :
        if (s + f) == pswrd :
            found = True
            break
print("YES" if found else  "NO")
