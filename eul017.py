def eul17(n):
    """If all the numbers from 1 to n = 1000 (one thousand) inclusive were written out in words,
    how many letters would be used?"""
    def get_digits(i):
        three = {1, 2, 6, 10}
        four = {4, 5, 9}
        five = {3, 7, 8, 40, 50, 60}
        six = {11, 12, 20, 30, 80, 90}
        seven = {15, 16, 70}
        eight = {13, 14, 18, 19}
        nine = {17}

        if i in three:
            return 3
        elif i in four:
            return 4
        elif i in five:
            return 5
        elif i in six:
            return 6
        elif i in seven:
            return 7
        elif i in eight:
            return 8
        elif i in nine:
            return 9
        else:
            return 0

    def inspect_num(m):
        digits = get_digits(m)

        if m == 1000:
            return 11
        elif m == 0:
            return 0
        elif digits != 0:
            return digits

        else:
            if m > 99:
                if m % 100 == 0:
                    return get_digits(int(m / 100)) + 7
                else:
                    return get_digits(int(m / 100)) + 10 + inspect_num(m % 100)
            else:
                return get_digits(m - (m % 10)) + inspect_num(m % 10)

    num = 0
    for d in range(1, n + 1):
        num += inspect_num(d)
    return num


print(eul17(1000))
# 21124
