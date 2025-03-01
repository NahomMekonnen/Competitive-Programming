# Problem: Python Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

from collections import defaultdict

if __name__ == '__main__':
    num = defaultdict(list)
    low = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        low.append(score)
        num[score].append(name)
    low = list(set(low))
    low.sort()    
    num[low[1]].sort()
    for i in num[low[1]] :
        print(i)