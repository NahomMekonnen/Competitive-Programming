class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = defaultdict(int)
        self.rows = rows

    def setCell(self, cell: str, value: int) -> None:
        self.sheet[cell] = value

    def resetCell(self, cell: str) -> None:
        self.sheet[cell] = 0

    def getValue(self, formula: str) -> int:
        x,y = formula.split("+")
        x = x[1:]
        if x.isdigit() and y.isdigit() :
            return int(x) + int(y)
        if x.isdigit() :
            return int(x) + self.sheet[y]
        if y.isdigit() :
            return int(y) + self.sheet[x]
        return self.sheet[x] + self.sheet[y]
