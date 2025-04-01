"""
Write code that creates a list of 52 tuples representing each card in a deck
with rank 2 - 14 for 2 - J, Q, K, A
"""

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
