def eul11():
    """What is the greatest product of four adjacent numbers in the same direction
    (up, down, left, right, or diagonally) in the 20×20 grid (largestProduct.txt)?"""
    text_file = open("resources/largestProduct.txt", "r")
    data = [[int(n) for n in line.split()] for line in text_file]
    text_file.close()

    max_product = 0
    # rows/columns
    for i in range(20):
        for j in range(16):
            product = data[i][j] * data[i][j + 1] * data[i][j + 2] * data[i][j + 3]
            if product > max_product:
                max_product = product
            product = data[j][i] * data[j + 1][i] * data[j + 2][i] * data[j + 3][i]
            if product > max_product:
                max_product = product

    # diagonals
    for i in range(16):
        for j in range(16):
            product = data[i][j] * data[i + 1][j + 1] * data[i + 2][j + 2] * data[i + 2][j + 3]
            if product > max_product:
                max_product = product
            product = data[i][19 - j] * data[i + 1][18 - j] * data[i + 2][17 - j] * data[i + 3][16 - j]
            if product > max_product:
                max_product = product

    return max_product


print(eul11())
# 70600674
