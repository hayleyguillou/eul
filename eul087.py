import math, itertools

def sieve(n):
    # returns all primes between 2 and n
    s = [True] * (n + 1)
    s[0], s[1] = False, False

    for i in range(2, int(math.sqrt(n))):
        curr = i + i
        while curr <= n:
            s[curr] = False
            curr += i
    return [i for i in range(len(s)) if s[i] is True]
    
p = sieve(int(math.sqrt((5*(10**7)) - 2**3 - 2**4)))
primes = [[q**2 for q in p], [q**3 for q in p], [q**4 for q in p]]

nums = set()
for i in range(len(p)):
    for j in range(len(p)):
        for k in range(len(p)):
            t = primes[0][i] + primes[1][j] + primes[2][k] 
            if t < 50000000:
                nums.add(t)
            else:
                break

print(len(nums))
