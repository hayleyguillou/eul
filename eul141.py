# brute force 

import math
squares = [x**2 for x in range(1, int(math.sqrt(100000)))]

s = 0
for n in squares:
    for d in range(1,n):
        q = int(n/d)
        r = n%d
        if r == 0:
            continue
        t = sorted([d,q,r])

        if t[2]/t[1] == t[1]/t[0]:
            s += n
            print(n, s)
            break

print (s)


# optimized

import fractions, math
      
limit = 10**12
prog = set()

for a in range(2,100000):
    for b in range(1,a):
        if (a**3 * b**2 + b**2 >= limit): break
        if fractions.gcd(a,b) != 1: continue
        
        c = 1
        n = a**3 * b * c**2 + c * b**2;
        while n <= limit:
            if int(math.sqrt(n))**2 == n:
                prog.add(n)
                print(n)
            c += 1
            n = a**3 * b * c**2 + c * b**2;
                
print(prog)
print(len(prog))
print(sum(prog))
