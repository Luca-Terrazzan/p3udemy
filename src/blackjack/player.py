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
        self.current_gamble = None

    def play(self, bet: int):
        """Plays a hand
        Arguments:
            bet {int} -- The amount to bet
        Raises:
            InvalidGamble -- If another hand is currently in play OR
                             an invalid amount has been passed
            BankruptException -- If a game is started with an empty bankroll
        """
        if self.current_gamble is not None:
            raise InvalidGamble("Hand not finished!")
        if bet < 1:
            raise InvalidGamble("Bet must be positive!")
        if bet > self.bankroll:
            raise BankruptException("Cannot gamble that much!")
        self.bankroll -= bet
        self.current_gamble = bet

    def win_hand(self):
        """Wins a hand
        Raises:
            InvalidGamble -- If no hands are currently in play
        """
        if self.current_gamble is None:
            raise InvalidGamble("Cannot play a hand without having bet!")
        self.bankroll += self.current_gamble * 2
        self.current_gamble = None

    def lose_hand(self):
        """Loses a hand
        """
        self.current_gamble = None

class BankruptException(Exception):
    """Raised when player acts with an empty bankroll
    """
    pass

class InvalidGamble(Exception):
    """Raised when an invalid gamble is performed
    """
    pass
