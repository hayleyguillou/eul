def eul2(n):
    """By considering the terms in the Fibonacci sequence whose values do not exceed n = four million, find the sum of
    the even-valued terms."""
    a, b, fib = 1, 2, []
    while b < n:
        a, b = b, a+b
        fib.append(a)
    
    return sum([x for x in fib if x % 2 == 0])

print(eul2(4000000))
# 4613732
