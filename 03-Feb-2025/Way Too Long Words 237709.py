# Problem: Way Too Long Words - https://codeforces.com/problemset/problem/71/A

n = int(input())
for i in range(n):
    word = input()
    if len(word) <= 10:
        print (word)
    else:
        print(f"{word[0]}{len(word)-2}{word[-1]}")