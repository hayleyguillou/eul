target = 100
ways = [0] * (target+1)
ways[0] = 1
 
for i in range(1,100):
    for j in range(i, target+1):
        ways[j] += ways[j - i]
    
print (ways[target])
