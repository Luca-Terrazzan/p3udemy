class Player():
    """Represents the human player
    """
    bankroll: int
    current_gamble: int

    def __init__(self, bankroll: int = 100):
        """Creates a player
        Keyword Arguments:
            bankroll {int} -- Player's starting bankroll (default: {100})
        """
        self.bankroll = bankroll

    def gamble_amount(self, amount: int):
        if amount > self.bankroll:
            raise BankruptException("Cannot gamble that much!")
        self.bankroll -= amount
        self.current_gamble = amount

    def win_hand(self):
        self.bankroll += self.current_gamble * 2

    def lose_hand(self):
        self.bankroll -= self.current_gamble * 2
        if self.bankroll <= 0:
            raise BankruptException("Game lost!")

class BankruptException(Exception):
    pass
