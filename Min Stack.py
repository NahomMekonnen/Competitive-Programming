class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minStack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1] :
            self.minStack.append(val)
       

    def pop(self) -> None:
        if self.stack[-1] == self.minStack[-1] :
            self.minStack.pop()
        self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1] 
