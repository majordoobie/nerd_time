"""
This module defines the hero template for the game

Classes
-------
    Hero:
        Hero inherits from the Character base class and defines unique methods for the character
"""
from abc import ABC
from typing import List

from packages.characters.character_abstract import Character
from packages.game_utils.utils import roll_dice


class Hero(Character, ABC):
    DEFAULT_HEALTH = 10
    DEFAULT_DIE_COUNT = 3
    DEFAULT_DIE_SIDES = 6
    DEFAULT_PIERCE_SHOT = False

    def __init__(self, username: str):
        super().__init__()
        self._pierce_shot = Hero.DEFAULT_PIERCE_SHOT
        self._name = username
        self._health = Hero.DEFAULT_HEALTH
        self._dice_count = Hero.DEFAULT_DIE_COUNT
        self._die_faces = Hero.DEFAULT_DIE_SIDES

    def combat_roll(self):
        """
        Return the combat rolls for attacking based on the amount of dice the monster has

        :return: None
        """
        rolls = []

        # check if pierce shot is activated, if it is, then rull all maxes
        if self.pierce_shot:
            for dice in range(0, self.dice_count):
                rolls.append(self.die_faces)

        else:
            for dice in range(0, self.dice_count):
                rolls.append(roll_dice(self.die_faces))
            # sort in descending order
            rolls.sort(reverse=True)

        # set the rolls
        self._combat_rolls = rolls

    @property
    def pierce_shot(self) -> bool:
        """
        Lucky Seven is a buff that can be activated in a hero using a LuckySeven potion. This will guarantee that the
        combat dice return all max values

        :return: Bool indicating if buff is enabled
        :rtype: bool
        """
        return self._pierce_shot

    @pierce_shot.setter
    def pierce_shot(self, value: bool) -> None:
        """
        Set the Lucky Seven buff

        :param value: Bool indicating if buff is in affect
        :return: LuckySeven bool
        """
        self._pierce_shot = value


    @property
    def damage(self) -> int:
        """
        Returns the amount of damage that is dealt when a successful attack is landed
        :return: Damage value
        :rtype: int
        """
        return self._damage

    @damage.setter
    def damage(self, value: int) -> None:
        """
        Sets the damage dealt by the hero
        :param value: Damage value to set
        :type value: int
        :return: None
        """
        self._damage = value

    @property
    def die_faces(self) -> int:
        """
        Return the number of faces the combat dice have for a Hero

        :return: Number of faces for the combat die
        :rtype: int
        """
        return self._die_faces

    @die_faces.setter
    def die_faces(self, value: int) -> None:
        """
        Set the number of faces the combat size have

        :param value: Number of faces on the die
        :return: None
        """
        if value < 4:
            raise ValueError("There must be at least 4 faces to a die")

        self._die_faces = value

    @property
    def dice_count(self) -> int:
        """
        Return the dice count for the Hero
        :return: Dice count
        :rtype: int
        """
        return self._dice_count

    @dice_count.setter
    def dice_count(self, value: int) -> None:
        """
        Set the number of combat dice the Hero has for combat.

        :param value: Number of dice
        :return: None
        :raises ValueError: When dice count is less than 1
        """
        if value < 1:
            raise ValueError("Dice count must at least be 1")

        self._dice_count = value
