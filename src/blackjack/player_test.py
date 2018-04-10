import unittest
from .player import Player, BankruptException

class PlayerTest(unittest.TestCase):
    def test_player_wins_hand(self):
        p = Player(50)
        p.play(1)
        p.win_hand()
        self.assertEqual(p.bankroll, 51)
        p.play(5)
        p.win_hand()
        self.assertEqual(p.bankroll, 56)

    def test_player_loses_hand(self):
        p = Player(50)
        p.play(1)
        p.lose_hand()
        self.assertEqual(p.bankroll, 49)
        p.play(5)
        p.lose_hand()
        self.assertEqual(p.bankroll, 44)

    def test_player_bankrupts(self):
        p = Player(2)
        p.play(2)
        p.lose_hand()
        with self.assertRaises(BankruptException):
            p.play(1)
