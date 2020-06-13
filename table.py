from errors import *


class Table(object):
    """Represents a object table supports different table styles french or american
    """

    def __init__(self, bias=[1]*37, rtype="f"):
        """Initialize the roulett table and all pockets
        bias - list with wheights for pockets
        rtype - either "f" for french or "a" for american roulette type"""
        self.bias = bias
        self.rtype = rtype
        self.pockets = {}

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

    def get_rtype(self):
        """returns roulette type"""
        return self.rtype

    def get_pocketnumbers(self):
        """returns all pocket numbers"""
        return self.pockets.keys()


test = Table(None, "a")
