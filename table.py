from errors import *
from ball import*


class Table(object):
    """Represents a object table supports different table styles french or american
    """

    def __init__(self, bias=[1]*38, rtype="f"):
        """Initialize the roulett table and all pockets
        bias - list with wheights for pockets
        rtype - either "f" for french or "a" for american roulette type"""
        self.bias = bias
        self.rtype = rtype
        self.pockets = {}
        self.history = []

        if rtype == "f":  # french roulette order
            pockets = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13,
                       36, 11, 30, 8, 23, 10, 5, 24, 16, 33, 1, 20, 14,
                       31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
            num = 0
            for pocket in pockets:
                num += 1
                if pocket == 0:
                    self.pockets[pocket] = [num, "g"]
                elif pocket % 2 == 0:
                    self.pockets[pocket] = [num, "r"]
                else:
                    self.pockets[pocket] = [num, "b"]
        elif rtype == "a":  # american order
            pockets = [0, 28, 9, 36, 30, 11, 7, 20, 32, 17, 5, 22, 34,
                       15, 3, 24, 36, 13, 1, "00", 27, 10, 25, 29, 12, 8,
                       19, 31, 18, 6, 21, 33, 16, 4, 23, 35, 14, 2]
            num = 0
            for pocket in pockets:
                num += 1
                if pocket == 0 or pocket == "00":
                    self.pockets[pocket] = [num, "g"]
                elif pocket % 2 == 0:
                    self.pockets[pocket] = [num, "b"]
                else:
                    self.pockets[pocket] = [num, "r"]
        else:
            raise RouletteTypeError("False Roulette Type")

    def get_bias(self):
        """returns bias list"""
        return self.bias

    def get_history(self):
        """returns the history of roulette outcomes"""
        return self.history

    def get_rtype(self):
        """returns roulette type"""
        return self.rtype

    def get_pocketnumbers(self):
        """returns all pocket numbers"""
        return self.pockets.keys()

    def get_pocket_color(self, num):
        """returns color for num"""
        if num == 0 or num == "00":
            return "g"
        elif num % 2 == 0:
            if self.get_rtype() == "f":
                return "r"
            else:
                return "b"
        else:
            if self.get_rtype() == "f":
                return "b"
            else:
                return "r"

    def play_round(self, player, debug=False):
        """plays a round of roulette
           player - the person playing the round"""
        # get players bet
        bets = player.get_current_bets()
        # play ball
        ball = Ball(self)
        # winning number
        winning_num = ball.throw_ball()
        # add to roulette history
        self.history.append(winning_num)
        # compare with player
        if debug:
            print("inside play_round")
            print(bets[0].get_colorc())
            print("ball obj: winning number:")
            print(winning_num)
        for bet in bets:
            # winning color inside loop to support betting on multiple tables
            winning_color = player.get_player_table().get_pocket_color(winning_num)
            if debug:
                print(winning_color)
                print(bet.get_colorc())
            bet_type = bet.get_type()
            # Single bets
            if bet_type == "Single" and winning_num == bet.get_pocketc():
                # pay out price
                player.change_player_balance(bet.get_bet_amount()*36)
            # Color bets
            elif bet_type == "Color" and winning_color == bet.get_colorc():
                # pay out price
                if debug:
                    print("winn!!!!!!!!!")
                player.change_player_balance(bet.get_bet_amount()*2)
            else:
                player.change_player_balance(-bet.get_bet_amount())
        player.del_current_bets()


test = Table(None, "a")
