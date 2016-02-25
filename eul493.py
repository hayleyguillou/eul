import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)
    
print(7 *(1 - nCr(60,20)/nCr(70,20)))

# E(X) 
# = E(col1+col2+...+col7) 
# then by linearity of expectation...
# = E(col1) + E(col2) + ... + E(col6)
# since there are equal numbers of each colour...
# = 7E(col1)                             
# = 7 * probability that a particular color is present
# = 7 * (1 - probability that a particular color is absent)
# = 7 * (1 - (# ways to pick 20 avoiding a color)/(# ways to pick 20))
# = 7 * (1 - (60 choose 20)/(70 choose 20))
