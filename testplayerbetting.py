from player import*
from table import*
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


sim_singleplayer(50, [5, 4, 9, 8], 1000, True,
                 True, [23, 33, 9], debug_text=False)
