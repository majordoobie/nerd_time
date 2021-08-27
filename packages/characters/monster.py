"""
Module represents a Monster character in the game

Classes
-------
    Monster:
        Monster inherits functionality from the Character class and adds its own unique functions
"""
from abc import ABC
from typing import List

from packages.characters.character_abstract import Character
from packages.game_utils.utils import roll_dice


class Monster(Character, ABC):
    def __init__(self, name: str, health: int, dice_count: int):
        super().__init__()
        self._name = name
        self._health = health
        self._dice_count = dice_count

    @property
    def dice_count(self) -> int:
        """
        Amount of dice the monster has for combat. The more dice, the higher chance they have
        to be successful in attacking or blocking

        :return: Number of combat die
        :rtype: int
        """
        return self._dice_count

    @dice_count.setter
    def dice_count(self, value: int) -> None:
        """
        Sets the dice count. Checks to make sure that the dice count is within the acceptable range

        :param int value: Number of dice to set
        :return: None
        :raises ValueError: Raised when dice count is not within the range of allowed dice count
        """
        if value not in range(Monster.MIN_DICE, Monster.MAX_DICE + 1):
            raise ValueError(f"{self.__class__.__name__} object may only carry between {Monster.MIN_DICE} and "
                             f"{Monster.MAX_DICE} number of dice.")

        self._dice_count = value

    def combat_roll(self) -> List[int]:
        """
        Return the combat rolls for attacking based on the amount of dice the monster has
        :return: List of rolls in descending order
        :rtype: List[int]
        """
        rolls = []
        for dice in range(0, self.dice_count):
            rolls.append(roll_dice())

        # sort in descending order
        rolls.sort(reverse=True)
        return rolls

