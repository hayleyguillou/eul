def eul15(n):
    """How many such routes are there through a n=20×20 grid?"""
    d = [[1 for x in range(n + 1)] for x in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            d[i][j] = d[i - 1][j] + d[i][j - 1]
    return d[n][n]

print(eul15(20))

