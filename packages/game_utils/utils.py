from random import randint


def roll_dice(sides: int = 6) -> int:
    """
    Return a dice roll using the randint function

    :param int sides: Number of sides the die contains
    :return: Random roll
    :rtype: int
    """
    if sides < 1:
        raise ValueError

    return randint(1, sides)
