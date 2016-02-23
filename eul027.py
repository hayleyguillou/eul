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

# n**2 + (a*n) + b
max_n = -1
max_set = (0,0)

y = 1000

for a in range(-y,y+1):
    for b in range(-y,y+1):
        n = 0
        prod = n**2 + (a*n) + b
        while prime(prod):
            n += 1
            prod = n**2 + (a*n) + b
        if n > max_n:
            max_n = n
            max_set = (a,b)
            print (max_n, max_set)
            
print(max_set[0]*max_set[1])
