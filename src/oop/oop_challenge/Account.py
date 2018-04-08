"""Account Class
Raises:
    Exception -- [description]
    Exception -- [description]
Returns:
    [type] -- [description]
"""
class Account():
    """Some account class
    """
    def __init__(self, owner: str, balance: float = 0.00):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        """Deposit a sum
        """
        if amount <= 0.00:
            raise Exception('Deposits must be made on positive amounts!')
        self.balance += amount

    def withdraw(self, amount: float):
        """Withdraw a sum
        """
        if amount < 0.00 or (self.balance < amount):
            raise Exception('Cannot withdraw the desired amount!')
        self.balance -= amount

    def __str__(self):
        return f'Account owner: {self.owner}. Account balance: {self.balance}'
