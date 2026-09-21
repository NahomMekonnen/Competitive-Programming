class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        subsS, subsT = defaultdict(int), defaultdict(int)    
        w = len(s) // k
        for i in range (0, len(s), w) :
            subsS[s[i:i+w]] += 1
            subsT[t[i:i+w]] += 1
        return subsS == subsT
          