import pylab as plt
from table import Table
from wallet import*
from player import*
from bet import*
# create table to bet on
import random
from errors import*


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
    Geldsack = Wallet(0, negative=True)
    history = []
    for i in range(50):
        Geldsack.change_wealth(bet.bet_single())
        history.append(Geldsack.get_wealth())
    endavg.append(history[-1])

    plt.plot([i for i in range(len(history))], history)
plt.title(f"End average = {(sum(endavg)/len(endavg))}")
plt.show()
