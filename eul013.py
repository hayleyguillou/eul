def eul13():
    """Work out the first ten digits of the sum of the following one-hundred 50-digit numbers (largeSum.txt)"""
    text_file = open("resources/largeSum.txt", "r")
    data = [int(n) for n in text_file]
    text_file.close()
    return int(str(sum(data))[0:10])


print(eul13())
