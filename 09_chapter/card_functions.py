"""
Using suits and ranks from the make_deck function, add functions to analyze
a hand of cards and identify:
Straight Flush
Four of a kind
Full house
Flush
Straight
Three of a kind
Two pair
Pair"""


SUITS = ("S",
         "C",
         "D",
         "H")
RANKS = tuple(range(2,15))


def make_deck():
    deckbuilder = []
    for suit in SUITS:
        for rank in RANKS:
            deckbuilder.append((rank, suit))
    return deckbuilder


def same_suit(hand):
    suit = hand[0][1]
    return all(card[1] == suit for card in hand))

def is_straight_flush(hand):
    sorted_hand = sorted(hand)
    for card in sorted_hand:
        if not same_suit(hand):
            return False
    if sorted_hand[0][0] + 4 != sorted_hand[4][0]:
        return False
    return True
    
            

def is_straight_flush(hand):
    