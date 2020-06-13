import pylab as plt
from table import Table
# create table to bet on
import random
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


class Bet(object):
    """parent class for bets holds amount of bet"""

    def __init__(self, amount, table, ball):
        """initialize bet amount"""
        self.amount = amount
        self.table = table
        self.ball = ball

    def get_bet_amount(self):
        """returns betamount"""
        return self.amount


class SingleBet(Bet):
    """Class for a single bet"""

    def __init__(self, pocketc, amount, table, ball):
        """initialize single bet"""
        super().__init__(amount, table, ball)
        self.pocketc = pocketc

    def get_pocketc(self):
        """return pocket of choice for current bet"""
        return self.pocketc

    def bet_rand_single(self):
        """bet on a random number"""
        pass

    def bet_single(self):
        """bet on a number"""
        if self.get_pocketc() == ball.throw_ball():
            return self.get_bet_amount()*36
        else:
            return self.get_bet_amount()*-1


class Ball(object):
    """Roulette ball"""

    def __init__(self, table):
        """Tabel - table obj either french or american"""
        # get pockets ball can land in
        self.pockets = table.get_pocketnumbers()

    def throw_ball(self):
        # list because .choice doesn't work on dicts
        return random.choice(list(self.pockets))


# get some money
# Geldsack = Wallet(1000)
# french testtable
testtable = Table(None, "a")
# init ball
ball = Ball(testtable)

# main betting
bet = SingleBet(0, 5, testtable, ball)  # bet on 0 with 2 dollars each

endavg = []
for t in range(1000):  # for 10 betting trials start with 1000$
    Geldsack = Wallet(150, negative=True)
    history = []
    for i in range(50):
        Geldsack.change_wealth(bet.bet_single())
        history.append(Geldsack.get_wealth())
    endavg.append(history[-1])

    plt.plot([i for i in range(len(history))], history)
plt.title(f"End average = {(sum(endavg)/len(endavg))}")
plt.show()
