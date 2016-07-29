import itertools


def eul59():
    """Decrypt the message and find the sum of the ASCII values in the original text."""
    cipher = [c.rstrip('\n') for c in open('resources/p059_cipher.txt')]
    cipher = [int(c) for c in cipher[0].split(",")]
    for key in itertools.product(range(97, 123), repeat=3):
        msg = [x ^ y for x, y in zip(cipher, itertools.cycle(key))]
        if ' the ' in ''.join(map(chr, msg)):
            return sum(msg)

print(eul59())
# 107359
