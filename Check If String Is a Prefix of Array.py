class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        word = ""
        for i in words:
            word += i
            if s == word :
                return True
        return False
