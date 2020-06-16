import random


class Ball(object):
    """Roulette ball"""

    def __init__(self, table):
        """Tabel - table obj either french or american"""
        # get pockets ball can land in
        self.pockets = list(table.get_pocketnumbers())
        self.bias = list(table.get_bias())

    def throw_ball(self):
        # list because .choice doesn't work on dicts
        return random.choice(list(self.pockets))

    def throw_ball_bias(self):
        """Throws ball considering bias"""
        while True:
            c = random.choice(list(self.pockets))
            indexc = self.pockets.index(c)
            if random.random() < self.bias[indexc]:
                return c
