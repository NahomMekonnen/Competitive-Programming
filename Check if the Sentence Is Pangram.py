class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        checker = "abcdefghijklkmnopqrstuvwxyz"
        return len(set(checker)) == len(set(sentence))
