# Enter your code here. Read input from STDIN. Print output to STDOUT
eng = input()
eNews = set(map(int, input().split()))
fren = input()
fNews = set(map(int,input().split()))
print(len(eNews.difference(fNews)))


