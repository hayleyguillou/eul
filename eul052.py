from eul import get_sorted_digits


def eul52():
    """Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits."""
    i = 1
    while 1:
        n = get_sorted_digits(2*i)
        if get_sorted_digits(3*i)== n:
            if get_sorted_digits(4*i) == n:
                if get_sorted_digits(5*i) == n:
                    if get_sorted_digits(6*i) == n:
                        break
        i += 1
    return i

print(eul52())
# 142857
