import eul


def eul25(n):
    """What is the index of the first term in the Fibonacci sequence to contain n = 1000 digits?"""
    index, a, b = 1, 0, 1
    while eul.num_len(b) < n:
        a, b = b, a + b
        index += 1
    return index

print(eul25(1000))
#4782
