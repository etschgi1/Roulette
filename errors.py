class Errors(Exception):
    """Class for custom error"""
    pass


class RouletteTypeError(Errors):
    """Error for invalid Roulette Type"""


class OutOfMoneyError(Errors):
    """When a player has no money left"""
