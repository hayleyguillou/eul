cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}


def score(hand):
    nums = sorted([cards.get(card[0]) for card in hand])

    if flush(hand):
        # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
        if nums[0] == 10:
            return 100, nums[4]

        # Straight Flush: All cards are consecutive values of same suit.
        if straight(nums):
            return 90, nums[4]

        return 60, nums[4]

    # Four of a Kind: Four cards of the same value.
    elif nums.count(nums[0]) == 4:
        return 80, nums[0]
    elif nums.count(nums[4]) == 4:
        return 80, nums[4]

    # Full House: Three of a kind and a pair.
    elif nums.count(nums[0]) == 2 and nums.count(nums[4]) == 3:
        return 70, nums[4]
    elif nums.count(nums[0]) == 3 and nums.count(nums[4]) == 2:
        return 70, nums[0]

    elif straight(nums):
        return 50, nums[4]

    # Three of a Kind: Three cards of the same value.
    elif nums.count(nums[2]) == 3:
        return 40, nums[2]

    # Two Pairs: Two different pairs.
    elif len(set(nums)) == 3:
        if nums.count(nums[4]) == 2:
            return 30, nums[4]
        else:
            return 30, nums[3]

    # One Pair: Two cards of the same value.
    elif len(set(nums)) == 4:
        i = 4
        while nums.count(nums[i]) != 2:
            i -= 1
        return 20, nums[i]

    # High card
    else:
        return nums[4], nums[4]


def flush(hand):
    # Flush: All cards of the same suit.
    suit = set([card[1] for card in hand])
    if len(suit) == 1:
        return True
    return False


def straight(nums):
    # Straight: All cards are consecutive values.
    if len(set(nums)) == 5 and nums[4] - nums[0] == 4:
        return True
    return False


def high_card(p1, p2):
    hand1 = sorted([cards.get(card[0]) for card in p1])
    hand2 = sorted([cards.get(card[0]) for card in p2])
    i = 4
    while i >= 0 and hand1[i] == hand2[i]:
        print(hand1[i], hand2[i])
        i -= 1
    return hand1[i] > hand2[i]
