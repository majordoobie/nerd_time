"""
This module defines the contract between all the character classes: Hero and Monsters

Classes
-------
    Character:
        Abstract class for game characters to enforce specific functions that all characters are required to have
"""
from abc import ABC, abstractmethod
from typing import List


class Character(ABC):
    MIN_DICE = 3
    MAX_DICE = 1
    DEFAULT_DAMAGE = 1

    def __init__(self):
        self._combat_rolls = []
        self._dice_count = 0
        self._name = ""
        self._dead = False
        self._health = 0
        self._damage = Character.DEFAULT_DAMAGE

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"

    @property
    def health(self) -> int:
        """
        Gets the current health of Character

        :return: Current health of character
        :rtype: int
        """
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        """
        Sets the health of the character. If health is below 1, then set character to dead. If character has health
        greater than 0, and character is dead, set character to alive.

        :param int value: Health value to set
        :return: None
        """
        self._health = value

        # set death if health is below 1; if death has been set and health is greater than 1, set to alive
        if value < 1:
            self.is_dead = True

        elif self.is_dead:
            self.is_dead = False

    @property
    def is_dead(self) -> bool:
        """
        Determine if the character is dead. A character is defined as dead when health is below 1

        :return: Bool indicating death
        :rtype: bool
        """
        return self._dead

    @is_dead.setter
    def is_dead(self, value: bool) -> None:
        """
        Sets character death bool
        :param bool value: Bool indicating death
        :return: None
        """
        self._dead = value

    @property
    def name(self) -> str:
        """
        Read only property representing the name of the character
        :return: Name of character
        :rtype: str
        """
        return self._name

    def takes_hit(self, damage=1) -> None:
        """
        Sets the characters new health after receiving damage

        :param damage: How much damage to decrement from the character health pool, defaults to 1
        :type damage: int
        :rtype: None
        """
        # Check if character is already dead
        if self.is_dead:
            raise ValueError("Character is already dead")

        # inflict damage
        self.health = self.health - damage

    @property
    @abstractmethod
    def dice_count(self) -> int:
        """
        Return the number of dice the character has for combat
        :return: Number of dice
        :rtype: int
        """
        pass

    @dice_count.setter
    @abstractmethod
    def dice_count(self, value: int) -> None:
        """
        Set the number of dice
        :param value: Number of dice
        :type value: int
        :return: None
        """
        pass

    @abstractmethod
    def combat_roll(self):
        """
        Set the combat rolls for determining if successful attack or defense

        :return: None
        """
        pass

    @property
    def combat_rolls(self) -> List[int]:
        return self._combat_rolls

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
        Sets the damage dealt by the character
        :param value: Damage value to set
        :type value: int
        :return: None
        """
        self._damage = value


