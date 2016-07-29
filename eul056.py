from eul import get_digit_sum


def eul56(n):
    """Considering natural numbers of the form, a^b, where a, b < n = 100, what is the maximum digital sum?"""
    max_sum = 0
    for a in range(1, n):
        for b in range(1, n):
            digit_sum = get_digit_sum(a**b)
            if digit_sum > max_sum:
                max_sum = digit_sum
    return max_sum

print(eul56(100))
# 972
