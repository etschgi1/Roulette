from wallet import*
from bet import SingleBet


class Player(object):
    """Models a player playing Roulette"""

    def __init__(self, table, startmoney, canHaveDebt):
        """Start money - Money player beginns with
           canHaveDebt - True/False if True player can accumulate debt"""
        # table object on which the player plays
        self.table = table
        self.startmoney = startmoney
        self.canHaveDebt = canHaveDebt
        self.Wallet = Wallet(self.startmoney, self.canHaveDebt)
        self.bet_history = []
        self.current_bets = []

    def get_current_balance(self):
        """returns the wallet balance of a given player"""
        return self.Wallet.get_wealth()

    def get_bet_history(self):
        """returns the bet history of the player"""
        return self.bet_history

    def get_current_bets(self):
        """returns the current bet of current round"""
        return self.current_bets

    def del_current_bets(self):
        """resets/delets current bets"""
        self.current_bets = []

    def change_player_balance(self, amount):
        """amount - figure by with wealth is changed 
        changes the players balance"""
        self.Wallet.change_wealth(amount)

    def bet(self, bet_amount, bet_type, choice=[0]):
        """bet_amount- amount of bet
           bet_type - type of bet ("Single",)
           choice - pocket(s) player plays a list defaults to 0 pocket
        adds bet to bet history"""
        if type(choice) != list:
            x = choice
            choice = []
            choice.append(x)
        # only one choice possible
        if bet_type == "Single" and len(choice) == 1:
            bet = SingleBet(choice, bet_amount, self.table, self)
        # add to bet history
        try:
            self.current_bets.append(bet)
            self.bet_history.append(bet)
        except:
            return
