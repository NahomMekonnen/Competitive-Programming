# Problem: A - Zoro’s Bounty Dilemma - https://codeforces.com/gym/594356/problem/A

for _ in range(int(input())) :
    s = set(input())
    ans = 0
    for i in s:
        if i == "<" :
            ans += 1
        if i  == ">" :
            ans += 2
    print("=" if ans == 0 else "<" if ans == 1 else ">" if ans == 2 else "?")
 