from .suits import Suit, Value

class Card():
    value: Value
    suit: Suit

    def __init__(self, val: Value, suit: Suit):
        self.value = val
        self.suit = suit

    def __str__(self):
        return f'{self.value.name} of {self.suit.name}'
