import eul


def eul32():
    """"Find the sum of all products whose multiplicand/multiplier/product identity can be written as a
    1 through 9 pandigital."""
    products = set()
    for product in range(1000, 10000):
        if len(set(eul.get_digits(product))) == len(str(product)):
            for i in eul.get_proper_divisors(product):
                j = int(product / i)
                test = ''.join([str(i), str(j), str(i*j)])
                if len(test) == 9 and eul.pandigital(test):
                    products.add(i*j)
    return sum(products)


print(eul32())
