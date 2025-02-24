# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

row, col  = map(int,input().split())
snake = []
for i in range(row) :
    if i % 2 == 0 :
        snake.append(["#"]*col)
    else :
        snake.append(["."]*col)
step = True
for i in range(1,row,2) :
    if step :
        snake[i][-1] = "#"
    else :
        snake[i][0] = "#"
    step = not step
for i in snake :
    print("".join(i))