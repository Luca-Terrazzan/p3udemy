"""Deck module
Classes:
* Deck
"""

from typing import Set
from .card import Card
from .suits import Suit, Value

class Deck():
    """Represents a deck of cards
    """

    cards: Set[Card] = set()

    def __init__(self):
        self.cards = Set[Card]
        print(self.cards.add)
        # self.cards.add(Card(Value.EIGHT, Suit.SPADES))
