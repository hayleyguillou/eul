chain = 0
d = 0

for i in range(1000, -1, -1):
    if chain > i:
        break
    
    remainders = [0] * i
    value = 1
    position = 0
 
    while remainders[value] == 0 and value != 0:
        remainders[value] = position
        value *= 10
        value %= i
        position += 1
    
 
    if position - remainders[value] > chain:
        chain = position - remainders[value]
        d = i
    
print(chain, d)
