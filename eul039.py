def eul39(n):
    """For which value of p ≤ n = 1000, is the number of solutions maximised?"""
    max_sols = 0
    result = 0

    for p in range(2, n + 1, 2):
        sols = 0;
        for a in range(2, int(p / 3)):
            if p * (p - 2 * a) % (2 * (p - a)) == 0:
                sols += 1
        if sols > max_sols:
            max_sols = sols
            result = p
    return result


print(eul39(1000))
# 840
