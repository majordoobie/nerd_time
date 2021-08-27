from enum import Enum

from packages.utils.utils import roll_dice


class InitiativeEnum(Enum):
    HERO = 0
    MONSTER = 1


class Environment:
    INITIATIVE_DIE_SIDES = 20

    def __init__(self, room_name: str, desc: str, level: int):
        self._room_name = room_name
        self._desc = desc
        self._level = level

    @property
    def room_name(self):
        """
        Name of the room

        :setter: Sets the name of the room
        :return: Name of the room
        :rtype: str
        """
        return self._room_name

    @room_name.setter
    def room_name(self, value: str):
        self._room_name = value

    @property
    def description(self):
        """
        Description of the environment to be displayed when a hero enters the environment

        :return: Description of room
        :setter: Sets the description
        :rtype: str
        """
        return self._desc

    @description.setter
    def description(self, value: str):
        self._desc = value

    @property
    def level(self):
        """
        Sets the difficulty level for the room
        :return: Difficulty level
        :setter: Sets the difficulty level
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, value: int):
        self._level = value

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
