"""Helper functions that do not fit anywhere better than here"""

from collections import namedtuple
from random import randint
from typing import List

JunkLoot = namedtuple("JunkLoot", "name, desc")


def get_junk_loot():
    """None consumable loot items a monster may drop"""
    return (
        JunkLoot("Bones", "Brittle bones, eeek!"),
        JunkLoot("Torn Leaves", "How this get in my bag?"),
        JunkLoot("Broken Lockpick", "Must be good for something, right?"),
        JunkLoot("Hoof", "The fuck..."),
        JunkLoot("Broken Twig", "Maybe I can start a fire with this."),
        JunkLoot("Patch of Fur", "Million more of these and I can make something useful.")
    )


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


def get_user_input(choices: List[int]) -> int:
    """Validate user input until the correct choice is made"""
    valid_input = False
    check_for_q = True if -1 in choices else False

    while not valid_input:
        result = input("DungeonDudes > ")
        if check_for_q:
            if result.lower() in ["Q", "q"]:
                return -1

        if result.isdigit():
            if int(result) in choices:
                return int(result)

        print(f"\n[!] Invalid input, try again...\n")


