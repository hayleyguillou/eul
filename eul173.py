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
        
        

print (sum(squares.values()))
