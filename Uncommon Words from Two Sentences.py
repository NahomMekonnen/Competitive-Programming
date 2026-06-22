
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = defaultdict(int)
        for i in s1.split(" ") :
            words[i] +=1
        for i in s2.split(" ") :
            words[i] +=1
        return [i for i in words if words[i] == 1]
