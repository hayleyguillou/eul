def eul42():
    """Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
    English words, how many are triangle words?"""

    with open('resources/p042_words.txt') as f:
        words = f.read().replace("\"", "").split(',')
        words.sort()

    triangles = [(0.5 * (i * (i + 1))) for i in range(50)]
    count = 0
    for word in words:
        if sum([ord(letter.lower()) - ord('a') + 1 for letter in word]) in triangles:
            count += 1
    return count

print(eul42())
# 162
