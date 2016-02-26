# BRUTE FORCE
one = []
for L in range(12, 50):
    count = 0
    for i in range(L - 2, L//3 - 1, -1):
        for j in range(L - i - 1, 0, -1):
            k = L - i - j
            if i >= j >= k:
                nums = sorted([i,j,k])
                if nums[0]**2 + nums[1]**2 == nums[2]**2:
                    count += 1
    if count == 1:
        one.append(L)
        
print (one)
