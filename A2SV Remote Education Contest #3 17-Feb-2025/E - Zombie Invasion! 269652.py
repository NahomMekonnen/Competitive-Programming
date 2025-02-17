# Problem: E - Zombie Invasion! - https://codeforces.com/gym/588094/problem/E

from collections import defaultdict

for _ in range(int(input())) :
    n , k = map(int,input().split())
    heal = list(map(int,input().split()))
    pos =list(map(int,input().split()))

    zombs = defaultdict(int)
    for i in range(len(pos)):
        zombs[abs(pos[i])] += heal[i]
    positions = sorted(zombs.keys())
    alive, prev, carry = True, 0, 0
    
    for i in range(len(positions)) :
        damage = (k * (positions[i] - prev)) + carry
        if damage < zombs[positions[i]] :
            alive = False
            break
        carry = damage - zombs[positions[i]]
        prev = positions[i]

    print("YES" if alive else "NO")
    
    # 1 2 3