"""Card module
Classes:
* Card
"""

from .suits import Suit, Value

class Card():
    """Represents a gaming card with a specific value and suit
    """

    value: Value
    suit: Suit

    def __init__(self, val: Value, suit: Suit):
        """Creates a card, notice that it uses a specific enumerator for both
        values and suits

        Arguments:
            val {Value} -- The card's value
            suit {Suit} -- The card's suit
        """

        self.value = val
        self.suit = suit

    def __str__(self) -> str:
        return f'{self.value.name} of {self.suit.name}'
