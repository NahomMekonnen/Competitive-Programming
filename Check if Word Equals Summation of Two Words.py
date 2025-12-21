class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        num1, num2 = "", ""
        for i in firstWord :
            num1 += str(ord(i)-ord("a"))
        for i in secondWord :
            num2 += str(ord(i)-ord("a"))
        word = int(num1) + int(num2)
        t = ""
        for i in targetWord :
            t += str(ord(i)-ord("a"))
        return word == int(t)
