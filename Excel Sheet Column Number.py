class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnNumber, base = 0, 0 
        for i in columnTitle[::-1] :
            num = ord(i) - ord("A") + 1
            num *= (26 ** base)
            columnNumber += num
            base += 1
        return columnNumber