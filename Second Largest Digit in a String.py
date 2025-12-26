class Solution:
    def secondHighest(self, s: str) -> int:
        n = set()
        for i in s :
            if i.isdigit() :
                n.add(int(i))
        return -1 if len(n) < 2 else sorted(list(n),reverse= True)[1]
        
