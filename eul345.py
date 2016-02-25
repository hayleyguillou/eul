import math, itertools


# BRUTE FORCE
matrix = [[  7,  53, 183, 439, 863],
          [497, 383, 563,  79, 973],
          [287,  63, 343, 169, 583],
          [627, 343, 773, 959, 943],
          [767, 473, 103, 699, 303]]

sq = int(math.sqrt(len(matrix)))
print("Size: " + str(sq))

max_sum = 0

for combo in itertools.permutations([x for x in range(sq)],sq):
    sum = 0
    for i in range(len(combo)):
        sum += matrix[i][combo[i]]
    if sum > max_sum:
        max_sum = sum
    
print (max_sum)
