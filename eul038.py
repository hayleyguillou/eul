def eul38():
    """What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer
     with (1,2, ... , n) where n > 1?"""
    pandigitals = []
    check = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
    for n in range(1, 100000):
        concat, i = "", 1
        while len(concat) < 10:
            concat += str(n * i)
            if len(concat) == 9:
                if set([int(x) for x in concat]) == check:
                    pandigitals.append(int(concat))
            i += 1
    return max(pandigitals)


print(eul38())
# 932718654
