import calendar


def eul19():
    """How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""
    return len([(year, month) for year in range(1901, 2000 + 1) for month in range(1, 12 + 1)
                if calendar.weekday(year, month, 1) == 6])


print(eul19())
# 171
