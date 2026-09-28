class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s :
            if i == ")" :
                left = deque()
                x = stack.pop()
                while x != "(" :
                    left.append(x)
                    x = stack.pop()
                while len(left) > 0 :
                    stack.append(left.popleft())
            else :
                stack.append(i)
        return "".join(stack)