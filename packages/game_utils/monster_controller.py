"""
Module controls spawning the correct creatures for the environment
"""
from collections import namedtuple
import csv
from math import ceil
from pathlib import Path
from random import choice
from typing import List

from packages.characters.monster import Monster

MONSTER_FILE = "data/.dd_monsters"
MonsterRecords = namedtuple("MonsterRecord", "name, health, dice_count, noise")
EnvironmentRecord = namedtuple("EnvironmentRecord", "level, habitable")


class MonsterController:
    def __init__(self, environment: EnvironmentRecord):
        """
        MonsterController spawns the monsters for the environment. Environments have dedicated monsters that spawn
        in them. MC will spawn at random, times a level modifier, the monsters that inhabit the environment

        :param environment: namedtuple containing information from the Environment
        :type environment: EnvironmentRecord(namedtuple)
        """
        self.env = environment
        self._monster_count = None
        self._monsters: List[Monster] = []
        self._habitable_monsters = _habitable_monsters(self.env)
        self._spawn_monsters()

    @property
    def monsters(self) -> List[Monster]:
        """
        Get the list of monsters spawned in the environment

        :return: List of monsters
        :rtype: List[Monster]
        """
        return self._monsters

    @property
    def monster_count(self) -> int:
        """
        Get the amount of monsters alive in the environment. When set to zero, all monsters are dead

        :return: Number of monsters
        :rtype: int
        """
        return self._monster_count

    def clean_up(self) -> None:
        """
        After a round of duels, clean up the dead monsters

        :return: None
        """
        def _key(item: Monster):
            if item.is_dead:
                return 1
            return 0

        # put the dead monsters at the end of the list
        self._monsters.sort(key=_key)

        # Pop the dead
        for index, creature in reversed(list(enumerate(self._monsters))):
            if creature.is_dead:
                self._monsters.pop(index)
                self._monster_count -= 1

    def _spawn_monsters(self):
        """Generate monsters based on environment level and habitat"""
        self._monsters = []
        self._monster_count = ceil(self.env.level / 2)
        for spawn in range(0, self.monster_count):
            monster = choice(self._habitable_monsters)
            self._monsters.append(
                Monster(monster.name, monster.health, monster.dice_count, monster.noise)
            )

        def _key(item: Monster):
            val = item.health + item.dice_count
            if item.noise:
                val *= 3
            return val

        self._monsters.sort(key=_key, reverse=True)


def _habitable_monsters(environment: EnvironmentRecord) -> List[MonsterRecords]:
    """Returns the list of monsters that inhabit an environment. If none are found, return monsters at random"""
    monster_path = Path(__file__).parent.resolve().parents[1] / Path(MONSTER_FILE)
    monster_repo = []

    if monster_path.exists():
        with monster_path.open("rt", encoding="utf-8") as infile:

            # check if the header is included, if it is, the seek will be set to the next line
            line = infile.readline()
            if not line.startswith("Name,StartHealth,DiceCount,MonsterNoise"):
                infile.seek(0)

            reader = csv.reader(infile)
            try:
                for creature in map(MonsterRecords._make, reader):
                    monster_repo.append(creature)
            except TypeError:
                print(f"Invalid read line detected in {monster_path.name}. Skipping line...")

    else:
        monster_repo = (
            MonsterRecords("Imp", 1, 1, None),
            MonsterRecords("BigImp", 2, 1, "roarrrr"),
            MonsterRecords("Mad Cow", 3, 1, "Mooooo"),
            MonsterRecords("Mad Cow", 3, 3, None),
        )

    habitable_monsters = []

    # If environment does not specify a list of creatures, then return the whole list
    if environment.habitable is None:
        habitable_monsters = monster_repo[:]
    else:
        for monster in monster_repo:
            if monster.name.lower() in (creature.lower() for creature in environment.habitable):
                habitable_monsters.append(monster)

    # If no matches are found, return the whole repo
    if not habitable_monsters:
        habitable_monsters = monster_repo[:]

    return habitable_monsters
