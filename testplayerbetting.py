from player import Player
from table import Table
import random


def show_results(tablename, playername):
    """shows results of all plays"""
    th, ph = tablename.get_history(), playername.get_bet_history()
    for h in th:
        p = ph[th.index(h)].get_pocketc()
        print(f"{h} --bet--> {p}", end=" ")
        if h == p:
            print("Won!!!")
        else:
            print()


def sim_singleplayer(runs, betamount,  start_money, debt=True, rand=False, betlist=[], roulette_type="f", debug_text=False):
    """run sim for singleplayer
        either with bets according to betlist or if rand == True with random bets
    Args:
        runs ([int]): [how often the roulette is played]
        betamount ([list]): [list of bet amount it cycles]
        rand (bool, optional): [True for random betnumberchoice]. Defaults to False.
        betlist (list, optional): [numbers to bet on]. Defaults to [].
    """
    table = Table(None, roulette_type)
    testsubject = Player(table, start_money, debt)
    run_count = 0
    for run in range(runs):
        if not rand:
            bl = len(betlist)
            choice = betlist[run_count % bl]
        else:
            choice = random.choice(list(table.get_pocketnumbers()))
        la = len(betamount)
        amount = betamount[run_count % la]
        testsubject.bet(amount, "Single", choice)
        table.play_round(testsubject)
        run_count += 1
    if debug_text:
        show_results(table, testsubject)


# sim_singleplayer(50, [5, 4, 9, 8], 1000, True, False,
#                 [1, 2, 3, 4, 5, 6], debug_text = True)

colortest = True
if colortest == True:
    # Test Color betting
    bias = [1]+[0]*36
    tisch = Table(bias)
    eli = Player(tisch, 500, True)
    print(f"before betting {eli.get_current_balance()}")
    eli.bet(10, "Color", "r")
    tisch.play_round(eli, True)
    print(eli.get_current_balance())

"""betlist not behaving proberly, probably betamount has bugs too"""
