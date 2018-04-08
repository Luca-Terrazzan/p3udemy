class Player():
    """Represents the human player
    """
    def __init__(self, bankroll: int = 100):
        """Creates a player
        Keyword Arguments:
            bankroll {int} -- Player's starting bankroll (default: {100})
        """
        self.bankroll = bankroll
