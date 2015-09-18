def eul14(n):
    """n → n/2 (n is even)
       n → 3n + 1 (n is odd)
       Which starting number, under n = one million, produces the longest chain?"""
    chains = [0] * (n+1)
    for i in range(1, n):
        chain = 1
        num = i
        while i > 1:
            if i % 2 != 0:
                i = 3*i + 1
            else:
                i /= 2
            chain += 1
        chains[num] = chain
    return chains.index(max(chains))

print(eul14(1000000))
# 837799
