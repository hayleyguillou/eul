def eul48(n):
    """Find the last ten digits of the series, 1 + 2 + 3 + ... + n = 1000."""
    return sum([(i**i) % (10**10) for i in range(1, n + 1)]) % (10**10)

print(eul48(1000))
# 9110846700
