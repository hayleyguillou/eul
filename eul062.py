import itertools, collections

def get_digits(n):
    return [int(i) for i in str(n)]

# 8 digits: 216 - 464
# 9 digits: 465 - 999


# cubes8 = [x**3 for x in range(216,465)]
# cubes9 = [x**3 for x in range(465,1000)]
# cubes10 = [x**3 for x in range(1000,2155)]
# cubes11 = [x**3 for x in range(2155,4642)]
cubes12 = [x**3 for x in range(4642,10000)]

test = {cube:int("".join((str(v) for v in sorted(get_digits(cube))))) for cube in cubes12}

ans = collections.Counter(test.values()).most_common(1)[0][0]

nums = []
for num, key in test.items():
    if key == ans:
        nums.append(num)
print(min(nums))    
