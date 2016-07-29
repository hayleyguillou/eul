from eul import palindrome, reverse_digits


def eul55(n):
    """How many Lychrel numbers are there below n = ten-thousand?"""
    lycs = []
    for num in range(1, n):
        i = num
        found, itr = False, 0
        while not found and itr < 50:
            i += reverse_digits(i)
            found = palindrome(i)
            itr += 1
        if not found:
            lycs.append(num)
    return len(lycs)

print(eul55(10000))
# 249
