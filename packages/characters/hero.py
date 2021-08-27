from abc import ABC
from typing import List

from packages.characters.character_abstract import Character


class Hero(Character, ABC):
    DEFAULT_HEALTH = 10
    DEFAULT_DIE_COUNT = 3
    DEFAULT_DIE_SIDES = 6

    def __init__(self, username: str):
        super().__init__()
        self._name = username
        self._health = Hero.DEFAULT_HEALTH
        self._dice_count = Hero.DEFAULT_DIE_COUNT
        self._die_faces = Hero.DEFAULT_DIE_SIDES

    def combat_roll(self) -> List[int]:
        pass

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
