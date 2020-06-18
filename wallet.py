from errors import*


class Wallet(object):
    """Wallet class for spending of player"""

    def __init__(self, wealth, negative=False):
        self.wealth = wealth
        self.negative = negative
        self.wealth_history = []
        self.wealth_history.append(wealth)

    def get_wealth(self):
        return self.wealth

    def change_wealth(self, money):
        self.wealth += money
        if self.negative == False:
            if self.wealth < 0:
                raise OutOfMoneyError("Player ran out of money!")
        # wealth histroy adder
        self.wealth_history.append(self.get_wealth())

    def get_wealth_history(self):
        """returns a list of players wealth history"""
        return self.wealth_history
