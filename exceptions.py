


class InvalidCardException(Exception):
    """Raised when an invalid card is created"""
    pass


class CardNotPlayableError(Exception):
    """Raised when a card cannot be played"""
    pass


class CardNotInPossessionError(Exception):
    """Raised when a player tries to play a card they don't have"""
    pass


class WinnerAlreadySetException(Exception):
    """Raised when trying to set a winner when one already exists"""
    pass