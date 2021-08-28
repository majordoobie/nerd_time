from collections import namedtuple
from enum import Enum
from typing import List, Optional

from packages.game_utils.utils import roll_dice
from packages.game_utils.monster_controller import MonsterController, EnvironmentRecord


class InitiativeEnum(Enum):
    HERO = 0
    MONSTER = 1


class Environment:
    INITIATIVE_DIE_SIDES = 20

    def __init__(self, room_name: str, desc: str, level: int, habitable: List[str] = None):
        """
        Create an environment and summon monsters based on level

        :param room_name: Name of the room
        :type room_name: str
        :param desc: Description of the room used to display to the user when they walk in
        :type desc: str
        :param level: Level of the room to increase the amount of monsters
        :type level: int
        """
        self._room_name = room_name
        self._desc = desc
        self._level = level
        self._habitable = habitable
        self._monsters = MonsterController(EnvironmentRecord(self.level, self.habitable))

    @property
    def monsters(self) -> MonsterController:
        """
        Returns the MonsterController instance
        :return: Monster controller
        :rtype: MonsterController
        """
        return self._monsters


    @property
    def habitable(self) -> Optional[List[str]]:
        """
        Return the list of habitable monsters of this environment. If none is given, then any monsters will spawn

        :return: List of monsters that exist in the environment
        :rtype: Optional[List[str]]
        """
        return self._habitable

    @property
    def room_name(self) -> str:
        """
        :return: Name of the room
        :rtype: str
        """
        return self._room_name

    @property
    def description(self) -> str:
        """
        Description of the environment to be displayed when a hero enters the environment

        :return: Description of the environment
        :rtype: str
        """
        return self._desc

    @property
    def level(self) -> int:
        """
        Sets the difficulty level for the room. This value will be used to determine how many monsters to spawn.

        :returns: Level of room
        :rtype: int
        """
        return self._level

    @staticmethod
    def initiative() -> InitiativeEnum:
        """
        Determines the combat initiative

        :return: Side that will attack first
        :rtype: InitiativeEnum
        """
        hero_initiative = 0
        monster_initiative = 0
        same_values = True

        # roll for initiative until we get different values
        while same_values:
            hero_initiative = roll_dice(Environment.INITIATIVE_DIE_SIDES)
            monster_initiative = roll_dice(Environment.INITIATIVE_DIE_SIDES)
            if hero_initiative != monster_initiative:
                same_values = False

        # return the highest initiative
        if hero_initiative > monster_initiative:
            return InitiativeEnum.HERO
        else:
            return InitiativeEnum.MONSTER
