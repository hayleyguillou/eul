import poker


def eul54():
    hands = [hand.rstrip('\n') for hand in open('resources/p054_poker.txt')]

    p1_count = 0
    p2_count = 0

    for line in hands:
        line = line.split(" ")

        p1 = line[:5]
        p2 = line[5:]

        s1 = poker.score(p1)
        s2 = poker.score(p2)

        if s1[0] > s2[0]:
            p1_count += 1
        elif s2[0] > s1[0]:
            p2_count += 1
        else:
            if s1[1] > s2[1]:
                p1_count += 1
            elif s2[1] > s1[1]:
                p2_count += 1
            else:
                if poker.high_card(p1, p2):
                    p1_count += 1
                else:
                    p2_count += 1
    return p1_count

print(eul54())
# 376
