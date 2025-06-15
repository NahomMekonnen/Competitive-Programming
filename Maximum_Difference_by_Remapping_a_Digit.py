class Solution:
    def minMaxDifference(self, num: int) -> int:
        num1, num2 = str(num), str(num)
        rep = ""
        for i in num1 :
            if i != "9" :
                rep = i
                break
        if rep != "" :
            num1 = num1.replace(rep,"9")
        for i in num2 :
            if i != "0" :
                rep = i
                break
        if rep != "" :
            num2 = num2.replace(rep,"0")
        return int(num1)-int(num2)
