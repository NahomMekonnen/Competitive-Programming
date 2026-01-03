class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops, stack = {"+","-","/","*"}, []
        for i in tokens :
            if i in ops :
                if len(stack) < 2 :
                    break
                num1, num2 = int(stack.pop()), int(stack.pop())
                op = 0
                if i == "+" :
                    op = num2 + num1
                elif i == "-" :
                    op = num2 - num1
                elif i == "*" :
                    op = num2 * num1
                else :
                    op = int(num2/num1)
                stack.append(op)
            else :
                stack.append(int(i))
        return stack[-1]
