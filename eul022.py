def eul22():
    """What is the total of all the name scores in the file (names.txt)?"""
    with open('resources/names.txt') as f:
        names = f.read().split(',')
        names.sort()
    return sum(i*sum(ord(c) - 64 for c in x.strip('"')) for i, x in enumerate(names, 1))


print(eul22())
