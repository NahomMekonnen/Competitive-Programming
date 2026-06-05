class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        word = ""
        for i in words:
            word += i + separator
        split = word.split(separator)
        return [i for i in split if i != ""]
