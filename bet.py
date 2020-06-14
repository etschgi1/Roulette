from ball import*


class Bet(object):
    """parent class for bets holds amount of bet"""

    def __init__(self, amount, table, player):
        """initialize bet amount"""
        self.amount = amount
        self.table = table

    def get_bet_amount(self):
        """returns betamount"""
        return self.amount


class SingleBet(Bet):
    """Class for a single bet"""

    def __init__(self, pocketc, amount, table, player):
        """initialize single bet"""
        super().__init__(amount, table, player)
        # if a longer list is entered, only betting with first number
        self.pocketc = pocketc[0]

    def get_type(self):
        """returns bet type"""
        return "Single"

    def get_pocketc(self):
        """return pocket of choice for current bet"""
        return self.pocketc

    def bet_rand_single(self):
        """bet on a random number"""
        pass
