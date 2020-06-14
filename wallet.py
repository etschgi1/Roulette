from errors import*


class Wallet(object):
    """Wallet class for spending of player"""

    def __init__(self, wealth, negative=False):
        self.wealth = wealth
        self.negative = negative

    def get_wealth(self):
        return self.wealth

    def change_wealth(self, money):
        self.wealth += money
        if self.negative == False:
            if self.wealth < 0:
                raise OutOfMoneyError("Player ran out of money!")
