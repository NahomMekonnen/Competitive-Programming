# Problem: Chat Order - https://codeforces.com/problemset/problem/637/B

time, messages = 0, dict()
for _ in range(int(input())) :
    message = input()
    time+=1
    messages[message]=time
ans = dict(sorted(messages.items(),key=lambda x : x[1], reverse= True))
for i in ans :
    print(i)