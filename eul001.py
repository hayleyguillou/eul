def eul1(n):
    """Find the sum of all the multiples of 3 or 5 below n = 1000."""
    return sum([x for x in range(1, n) if x % 3 == 0 or x % 5 == 0])

print(eul1(1000))
# 233168
