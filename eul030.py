import eul


def eul30():
    """Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."""
    return sum([x for x in range(2, 1000000) if sum([y**5 for y in eul.get_digits(x)]) == x])

print(eul30())
# 443839
