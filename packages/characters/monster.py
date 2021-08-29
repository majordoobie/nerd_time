"""
Module represents a Monster character in the game

Classes
-------
    Monster:
        Monster inherits functionality from the Character class and adds its own unique functions
"""
from abc import ABC
from random import random, randint, choice
from typing import List, Optional

from packages.characters.character_abstract import Character
from packages.environments.consumable_loot import CONSUMABLE_LOOT
from packages.environments.loot import Loot
from packages.game_utils.utils import roll_dice, get_junk_loot


class Monster(Character, ABC):
    def __init__(self, name: str, health: int, dice_count: int, noise: str = None):
        super().__init__()
        self._name = name
        self._health = health
        self._dice_count = dice_count
        self._noise = noise
        self._generate_loot()

    @property
    def noise(self) -> Optional[str]:
        """
        Returns the monster noise if available
        :return: Monster noise string
        :rtype: Optional[str]
        """
        return self._noise

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

    def combat_roll(self) -> None:
        """
        Return the combat rolls for attacking based on the amount of dice the monster has

        :return: None
        """
        rolls = []
        for dice in range(0, self.dice_count):
            rolls.append(roll_dice())

        # sort in descending order
        rolls.sort(reverse=True)

        # set the rolls
        self._combat_rolls = rolls

    def set_loot(self, value: Loot) -> None:
        """Add loot to inventory regardless of duplication"""
        self._loot.append(value)

    def _generate_loot(self):
        # check if the chance is height enough to loot
        modifier = (self.health + self.dice_count) * .1
        modifier = 1

        if not random() < modifier:
            return

        junk_loot = get_junk_loot()
        consumable_loot = CONSUMABLE_LOOT

        count = randint(0, 3)
        for _ in range(0, count):
            loot = choice(junk_loot)
            self.set_loot(
                Loot(
                    name=loot.name,
                    desc=loot.desc,
                    qty=randint(2, 20)
                )
            )

        # chance it again to see if good loot is dropped
        count = randint(0, 3)
        for _ in range(0, count):
            self.set_loot(choice(consumable_loot)())


