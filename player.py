from wallet import*
from bet import SingleBet, ColorBet


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

    def get_player_table(self):
        """returns the table obj the player plays on"""
        return self.table

    def get_wallet(self):
        """returns the wallet of a player"""
        return self.Wallet

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
        """bet_amount - amount of bet
           bet_type - type of bet("Single",)
           choice - pocket(s) player plays a list defaults to 0 pocket
        adds bet to bet history"""
        # choice will be outputed as list
        if type(choice) != list:
            x = choice
            choice = []
            choice.append(x)
        # only one choice possible
        if bet_type == "Single" and len(choice) == 1:
            bet = SingleBet(choice, bet_amount, self.table, self)

        if bet_type == "Color" and len(choice) == 1:
            bet = ColorBet(choice, bet_amount, self.table, self)
        # add to bet history
        try:
            self.current_bets.append(bet)
            self.bet_history.append(bet)
        except:
            return
            print("----debug no bet added to betlist----")

    def update_balance(self, winner_num, winner_col):
        """updates balance after each round"""
        if self.current_bets:
            for bet in self.current_bets:
                won = False
                bet_type = bet.get_type()
                if bet_type == "Single" and winner_num == bet.get_pocketc():
                    self.change_player_balance(bet.get_bet_amount()*35)
                    won = True
                if bet_type == "Color" and winner_col == bet.get_colorc():
                    self.change_player_balance(bet.get_bet_amount())
                    won = True
                if won == False:
                    self.change_player_balance(-bet.get_bet_amount())
            self.del_current_bets()
        else:
            print("No current bets placed can't update")


class SimPlayer(Player):
    """Models a Sim Player has a number"""

    def __init__(self, table, startmoney, canHaveDebt, number):
        # super init
        super().__init__(table, startmoney, canHaveDebt)
        self.number = number

    def get_SimPlayer_Number(self):
        """returns the number for a given SimPlayer"""
        return self.number
