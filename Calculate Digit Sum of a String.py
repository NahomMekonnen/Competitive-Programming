class Solution:
    def digitSum(self, s: str, k: int) -> str:
        
        while len(s) > k :
            split = []
            new_s = ""
            
            for i in range(0, len(s), k) :
                if i + k >= len(s) :
                    split.append(s[i:])
                else :
                    split.append(s[i:i+k])
            for i in range(len(split)) :
                num = sum([int(x) for x in split[i]])
                new_s += (str(num))
            s = new_s

                
        return s