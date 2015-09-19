import eul


def eul16(n):
    """What is the sum of the digits of the number 2^n = 1000?"""
    return sum([x for x in eul.get_digits(2**n)])

print(eul16(1000))
# 1366
