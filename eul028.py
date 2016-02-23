sq_size = 1001
iterations = int((sq_size - 1) / 2)

sum = 1
curr = 1
adder = 2

for i in range(iterations):
    for j in range(4):
        curr += adder
        sum += curr
    adder += 2
    
print(sum)
