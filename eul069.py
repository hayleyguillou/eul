import eul
sieve = eul.sieve_array(100000000)
total = 0
for n in range(2, 100000000, 2):
    prime = True
    for d in eul.get_factors(n):
        if not sieve[d + n/d]:
            prime = False
            break
    if prime:
        total += n
        print(n, total)
