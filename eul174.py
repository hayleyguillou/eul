squares = {x:0 for x in range(1,1000001)}

#print (len(squares))


for size in range(1, 10**6//4 +10):

    
    total = size**2
    
    size -= 2
    while size > 0:
        tmp = total - size**2 
        if tmp not in squares.keys():
            break
        squares[tmp] += 1
        size -= 2
        

sum = 0
for key, val in squares.items():
    if val != 0 and val <= 10:
        sum += 1
        
print(sum)
