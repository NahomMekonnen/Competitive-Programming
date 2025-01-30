# Problem: Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    myList = []
    for i in range(N):
        command = input().split()
        
        if command[0] == 'insert':
            myList.insert(int(command[1]),int(command[2]))
        elif command[0] == 'print':
            print(myList)
        elif command[0] == 'remove':
            myList.remove(int(command[1]))
        elif command[0] == 'append':
            myList.append(int(command[1]))
        elif command[0] == 'sort':
            myList.sort()
        elif command[0] == 'pop':
            myList.pop()
        elif command[0] == 'reverse':
            myList.reverse()