# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
my_dict = defaultdict(list)
n, m = list(map(int, input().split()))

for i in range(1,n+1) :
    my_dict[input()].append(i)
for i in range(m) :
    word=input()
    print(*my_dict[word] if word in my_dict else [-1])
    
