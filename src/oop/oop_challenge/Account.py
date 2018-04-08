class Account():
    """Account class
    Used in python3 course assignment
    """
    def __init__(self, owner: str, balance: float = 0.00):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0.00:
            raise Exception('Deposits must be made on positive amounts!')
        self.balance += amount

    def withdraw(self, amount: float):
        if amount < 0.00 or (self.balance < amount):
            raise Exception('Cannot withdraw the desired amount!')
        self.balance -= amount

    def __str__(self):
        return f'Account owner: {self.owner}. Account balance: {self.balance}'
