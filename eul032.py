import eul


def eul32bf():
    products = set()
    check = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for i in range(1, 10000):
        for j in range(1, int(100000/i)):
            if eul.num_len(i) + eul.num_len(j) + eul.num_len(i*j) == 9:
                if (set(eul.get_digits(i)).union(set(eul.get_digits(j)))).union(set(eul.get_digits(i * j))) == check:
                    products.add(i * j)
    return sum(products)


def eul32():
    products = set()
    check = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for product in range(100000, 1000, -1):
        for i in eul.get_proper_divisors(product)[:]:
            j = product / i
            if len(str(i)) + len(str(j)) + len(str(i * j)) == 9:
                if (set(eul.get_digits(i)).union(set(eul.get_digits(j)))).union(
                        set(eul.get_digits(product))) == check:
                    products.add(product)
                    print(products)
    return sum(products)


print(eul32bf())
