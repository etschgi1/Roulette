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


class ColorBet(Bet):
    """Class to model betting on either red or black
    """

    def __init__(self, colorc, amount, table, player):
        """initialize color_bet
        Args:
            colorc ([list]): [either "r" for red or "b" for black, only index 0 is taken]
            amount ([int]): [Money amount for bet]
            table ([table_obj]): [table on which the bet is placed]
            player ([player_obj]): [player that bets]
        """
        super().__init__(amount, table, player)
        if colorc[0] != "r" and colorc[0] != "b":
            colorc[0] = "colorerror"
        self.colorc = colorc[0]

    def get_type(self):
        """returns bet type"""
        return "Color"

    def get_colorc(self):
        """returns the choosen color"""
        return self.colorc
