# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        ans = sorted(words, key = lambda word : int(word[-1]))
        return ' '.join(word[:-1] for word in ans)