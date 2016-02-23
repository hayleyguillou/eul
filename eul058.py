import math

def prime(n):
    n = int(n)
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(math.sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

sq_size = 1001
iterations = int((sq_size - 1) / 2)


num_diag = 5
num_primes = 3
curr = 9
adder = 4

while num_primes/num_diag > 0.1:
    for j in range(4):
        curr += adder
        num_diag += 1
        if prime(curr):
            num_primes += 1
    adder += 2

    
print(adder - 1)
