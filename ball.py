import random


class Ball(object):
    """Roulette ball"""

    def __init__(self, table):
        """Tabel - table obj either french or american"""
        # get pockets ball can land in
        self.pockets = table.get_pocketnumbers()

    def throw_ball(self):
        # list because .choice doesn't work on dicts
        return random.choice(list(self.pockets))
