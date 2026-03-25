class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        c = Counter(s)
        return len(set([c[i] for i in c])) == 1
