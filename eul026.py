def eul26(n):
    """Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."""
    chain = 0
    d = 0

    for i in range(n, -1, -1):
        if chain > i:
            break

        remainders = [0] * i
        value = 1
        position = 0

        while remainders[value] == 0 and value != 0:
            remainders[value] = position
            value *= 10
            value %= i
            position += 1

        if position - remainders[value] > chain:
            chain = position - remainders[value]
            d = i
    return d

print(eul(1000))
# 983
