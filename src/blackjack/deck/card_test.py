import unittest
from .card import Card
from .suits import Value, Suit

class CardTest(unittest.TestCase):
    def test_card_creation(self):
        card1 = Card(Value.EIGHT, Suit.SPADES)
        self.assertEqual(card1.__str__(), 'EIGHT of SPADES')
