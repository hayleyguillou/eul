def eul6(n):
    """Find the difference between the sum of the squares of the first n = one hundred natural numbers and the
    square of the sum."""
    return sum([x for x in range(1, n + 1)])**2 - sum([x**2 for x in range(1, n + 1)])

print(eul6(100))
# 25164150
