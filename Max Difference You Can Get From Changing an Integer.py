class Solution:
    def maxDiff(self, num: int) -> int:
        a, b = str(num), str(num)
        x = ""
        for i in a :
            if i != "9" :
                x = i
                break
        if x != "" :
            a = a.replace(i,"9")
        x = ""
        for i in b :
            if i != "1" and i != "0" :
                x = i
                break
        
        if x != "" :
            if int(b.replace(i,"0")) == 0 or b[0] == i :
                b = b.replace(i,"1")
            else: 
                b = b.replace(i,"0")
            
        return int(a) - int(b)
