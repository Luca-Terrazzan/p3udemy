import unittest
from .deck import Deck

class CardTest(unittest.TestCase):
    def test_deck_creation(self):
        deck1 = Deck()
        print(f'Deck has these cards: {deck1}')
