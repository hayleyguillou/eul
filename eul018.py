def eul18():
    """Find the maximum total from top to bottom of the triangle below (maximumPath1.txt):"""
    text_file = open("resources/maximumPath1.txt", "r")
    data = [[int(n) for n in line.split()] for line in text_file]
    text_file.close()

    for i in range(len(data) - 2, -1, -1):
        for j in range(len(data[i])):
            data[i][j] += max(data[i + 1][j], data[i + 1][j + 1])
    return data[0][0]


print(eul18())
