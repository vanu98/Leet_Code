class Solution:
    def dayOfYear(self, date: str) -> int:
        count_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year,month,day = date.split('-')
        y = int(year)
        if (y % 400) == 0 or ((y % 4 == 0) and (y % 100 != 0)): count_days[1] = 29
        return sum(count_days[:int(month)-1])+int(day)
