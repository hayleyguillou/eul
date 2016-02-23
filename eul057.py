import math

def num_len(n):
    return int(math.log10(n)) + 1

count = 0

for i in range (1,1001):
    num = 1
    den = 2
    for j in range(i-1, 0, -1):
        num += 2 * den
        tmp = den
        den = num
        num = tmp
    # SAVE THE NUMBER HERE FOR THE NEXT ITERATION
    num += den
    
    if num_len(num) > num_len(den):
        count += 1
        
print(count)
