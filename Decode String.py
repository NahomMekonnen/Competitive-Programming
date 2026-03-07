class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s) :
            j = i + 1
        
            if s[i].isnumeric() :
                while j < len(s) and s[j].isnumeric() :
                    j += 1
                stack.append(int(s[i:j]))
                i = j
                j = i + 1
            
            elif s[i].isalpha() :
                while j < len(s) and s[j].isalpha() :
                    j += 1
                stack.append(s[i:j])
                i = j
                j = i + 1
            
            elif i < len(s) and s[i] == "[" :
                stack.append(s[i])
                i += 1

            elif i < len(s) and s[i] == "]" :
                words = []
                while stack[-1] != "[" :
                    words.append(stack.pop())
                stack.pop()
                num = stack.pop()
                words = "".join(words[::-1])
                stack.append(words * num)
                i += 1

        return "".join(stack)
