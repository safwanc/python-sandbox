import random

def single_riffle(deck_of_cards):
    halfway = len(deck_of_cards) // 2
    half1, half2 = deck_of_cards[:halfway], deck_of_cards[halfway:]
    shuffled_deck = list()

    temp1, temp2 = half1[:], half2[:]

    while half1 or half2:
        if half1:
            for _ in range(random.randint(1, len(half1))):
                shuffled_deck.append(half1.pop())

        if half2:
            for _ in range(random.randint(1, len(half2))):
                shuffled_deck.append(half2.pop())

    return shuffled_deck, temp1, temp2

deck = list(range(1, 53))
shuffled_deck, half1, half2 = single_riffle(deck)