def eul28(n):
    """What is the sum of the numbers on the diagonals in a n*n(= 1001 * 1001) spiral formed by
    starting with the number 1 and moving to the right in a clockwise direction?"""

    iterations = int((n - 1) / 2)
    s, curr, adder = 1, 1, 2

    for i in range(iterations):
        for j in range(4):
            curr += adder
            s += curr
        adder += 2
    return s

print(eul28(1001))
# 669171001
