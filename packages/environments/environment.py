from enum import Enum

from packages.game_utils.utils import roll_dice


class InitiativeEnum(Enum):
    HERO = 0
    MONSTER = 1


class Environment:
    INITIATIVE_DIE_SIDES = 20

    def __init__(self, room_name: str, desc: str, level: int):
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
