"""Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
    x^2 - Dy^2 = 1"""
import math
from eul import perfect_sq, even, sieve
#
# def get_m(a,b,k):
#     n = 0
#     k = abs(k)
#     a = a % k
#     while (a + b*n) % k != 0:
#         n += 1
#     return n
#
# # chakravala method
# # (a*m + N*b)/k - (a + b*m)/k = (m**2 - N)/k
#
# max_x = 0
# i = 0
#
# for d in sieve(1000):
#     p, k, x1, y, sd = 1, 1, 1, 0, math.sqrt(d)
#
#     while k != 1 or y == 0:
#         p = k * (p/k+1) - p
#         p = p - int((p - sd)/k) * k
#
#         x = (p*x1 + d*y) / abs(k)
#         y = (p*y + x1) / abs(k)
#         k = (p*p - d) / k
#         x1 = x
#
#
#     print(i, max_x)
#
#     if x > max_x:
#         max_x = x
#         i = d
# print (i, max_x)

def pell(d):
    p, k, x1, y, sd = 1, 1, 1, 0, math.sqrt(d)

    while k != 1 or y == 0:
        p = k * (p/k+1) - p
        p = p - int((p - sd)/k) * k

        x = (p*x1 + d*y) / abs(k)
        y = (p*y + x1) / abs(k)
        k = (p*p - d) / k
        x1 = x
    return x

L = 1000
print ("Project Euler 66 Solution:", max((pell(d),d) for d in sieve(L)))