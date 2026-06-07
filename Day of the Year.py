class Solution:
    def dayOfYear(self, date: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year, month, day = map(int, date.split("-"))
        if year % 4 == 0:
            if year % 100 == 0 :
                if year % 400 == 0 :
                    months[1] = 29
            else :
                months[1] = 29
        if month == 1 :
            return day
        return sum(months[:month-1]) + day
