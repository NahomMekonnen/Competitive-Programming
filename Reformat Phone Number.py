class Solution:
    def reformatNumber(self, number: str) -> str:
        n = ""
        for i in number : 
            if i.isnumeric() :
                n += i
        blocks = []
        if len(n) % 3 == 0 :
            for i in range(0, len(n) - 3 + 1, 3) :
                blocks.append(n[i:i+3]) 

        elif len(n) % 3 == 1 :
            for i in range(0, len(n) - 4, 3) :
                blocks.append(n[i:i+3])
            blocks.append(n[-4:-2])
            blocks.append(n[-2:])        
        else : 
            for i in range(0, len(n) - 2, 3) :
                blocks.append(n[i:i+3])
            blocks.append(n[-2:])

        return "-".join(blocks)