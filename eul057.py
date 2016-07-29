from eul import num_len


def eul57(n):
    """In the first n = one-thousand expansions,
    how many fractions contain a numerator with more digits than denominator?"""
    count = 0
    for i in range(1, n+1):
        num = 1
        den = 2
        for j in range(i-1, 0, -1):
            num += 2 * den
            tmp = den
            den = num
            num = tmp
        num += den

        if num_len(num) > num_len(den):
            count += 1
    return count

print(eul57(1000))
# 153
