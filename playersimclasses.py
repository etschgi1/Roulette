from table import Table
from player import Player, SimPlayer
import random
import pylab as plt
import statistics as stat

# random seed
# random.seed(1)


class Playersim(object):
    """Parent class to model the basic characteristics of a simulated Player"""

    def __init__(self, tablebias, tabletype, startmoney, canHaveDebt, betting_amount, maxrounds, playercount):
        """[initialize  a Playersim which initializes  playercount player and plays maxrounds of ]

        Args:
            tablebias ([list]): [bias for the roulette table]
            tabletype ([str]): [type of roulette table to initialize]
            startmoney ([int]): [money every player starts with]
            canHaveDebt ([bool]): [ability for players to have debt]
            betting_amount ([int]): [amount of money player will bet every round]
            maxrounds ([int]): [maximum of rounds player plays if he is not elimineted earlier (if canHaveDebt = Fasle)]
            playercount ([int]): [How many players are simulated]
        """
        self.tablebias = tablebias
        self.tabletype = tabletype
        self.startmoney = startmoney
        self.canHaveDebt = canHaveDebt
        self.betting_amount = betting_amount
        self.maxrounds = maxrounds
        self.playercount = playercount
        # list for simplayers
        self.simplayers = []
        # init table
        """Note every player plays on same table"""
        self.simtable = Table(self.tablebias, self.tabletype)
        self.tablepockets = self.simtable.get_all_pockets()
        # init players
        for playernum in range(self.playercount):
            self.simplayers.append(
                SimPlayer(self.simtable, self.startmoney, self.canHaveDebt, playernum))

    def basic_sim(self, bettype, debug=False, plothist=False, plotlin=False, plotmean=False, returnmean=False):
        """run a basic sim where every player bets one random number"""
        for run in range(self.maxrounds):
            for player in self.simplayers:
                # random choice
                if bettype == "Single":
                    choice = random.choice(list(self.tablepockets.keys()))
                elif bettype == "Color":
                    choice = random.choice(["r", "b"])
                player.bet(self.betting_amount, "Color", choice)
            num, col = self.simtable.play_round_new()
            for player in self.simplayers:
                # update
                player.update_balance(num, col)

                if debug:
                    print(player.get_SimPlayer_Number(),
                          player.get_current_balance())
        # all wealth histories:
        if True:  # plothist or plotlin or plotmean:
            wealthhistory = []
            for player in self.simplayers:
                wealthhistory.append(player.get_wallet().get_wealth_history())
        if plothist:
            out = [x[-1] for x in wealthhistory]

            print(f"mean: {stat.mean(out)} stdev: {stat.stdev(out)}")
            plt.hist(out)
            plt.show()

        if plotlin:
            x = list(range(self.maxrounds+1))
            y = wealthhistory
            m = []
            for l in y:
                plt.plot(x, l)
                m.append(l[-1])
            plt.title(f"Mean: {sum(m)/len(m)}")
            plt.show()
        if returnmean:
            return sum([l[-1]for l in wealthhistory])/len(wealthhistory)
        if plotmean:
            x = list(range(self.maxrounds+1))


test = Playersim([1]*38, "f", 0, True, 10, 50, 100)
m = test.basic_sim("Color", plotlin=True, returnmean=True)
print(f"Mean returnmean test: {m}")
