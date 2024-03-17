# Enter your code here. Read input from STDIN. Print output to STDOUT
set1 = set(map(int, input().split()))
verdict = True
n = int(input())
for i in range(n):
    set2 = set(map(int, input().split()))
    verdict = verdict and (set1>set2)

print(verdict)
