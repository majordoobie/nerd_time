from abc import ABC, abstractmethod

from packages.environments.loot import Loot
from packages.characters.hero import Hero


class ConsumableLoot(Loot, ABC):
    @abstractmethod
    def consume(self, hero: Hero) -> None:
        """
        Define how to handle "consuming" a loot object
        :param hero: The hero to apply the consumable to
        :return: None
        """
        pass

    @abstractmethod
    def remove_affect(self, hero: Hero) -> None:
        """
        Remove the temporary affect of whatever consumable was taken
        :param hero: The hero to apply the consumable to
        :return: None
        """
        pass


class AttackPotion(ConsumableLoot, ABC):
    DESC = """Increase the number of attacked dice by 1"""
    NAME = "Attack Potion"

    def __init__(self):
        super().__init__(AttackPotion.NAME, AttackPotion.DESC)

    def consume(self, hero: Hero) -> None:
        """
        Increments the dice count of the hero by 1

        :param hero: Hero to affect
        :return: None
        """
        hero.dice_count += 1

    def remove_affect(self, hero: Hero) -> None:
        """
        Restores the affects of the consumable

        :param hero: Hero to affect
        :return: None
        """
        hero.dice_count -= 1


