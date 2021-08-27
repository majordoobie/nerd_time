from abc import ABC, abstractmethod
from math import ceil

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


class LuckySeven(ConsumableLoot, ABC):
    DESC = """Increase the number of faces of the combat die by a factor of 2"""
    NAME = "LuckySeven"

    def __init__(self):
        super().__init__(LuckySeven.NAME, LuckySeven.DESC)

    def consume(self, hero: Hero) -> None:
        hero.die_faces *= 2

    def remove_affect(self, hero: Hero) -> None:
        hero.die_faces /= 2


class HealthPotion(ConsumableLoot, ABC):
    DESC = """Increase health by 50% of missing health"""
    NAME = "HealthPotion"

    def __init__(self):
        super().__init__(HealthPotion.NAME, HealthPotion.DESC)

    def consume(self, hero: Hero) -> None:
        """
        Increase the hero health by 50% of the missing health.
        :param hero: Hero to affect
        :return: None
        """
        max_health = hero.DEFAULT_HEALTH
        difference = max_health - hero.health
        increase_health = ceil(difference * .5)
        hero.health += increase_health

    def remove_affect(self, hero: Hero) -> None:
        """Abstract method not implemented by this consumable"""
        pass


class HeavyHand(ConsumableLoot, ABC):
    DESC = """Increase the amount of damage dealth by 1"""
    NAME = "HeavyHand"

    def __init__(self):
        super().__init__(HeavyHand.NAME, HeavyHand.DESC)

    def consume(self, hero: Hero) -> None:
        """
        Increase the base damage of hero by 1
        :param hero: Hero to affect
        :return:None
        """
        hero.damage += 1

    def remove_affect(self, hero: Hero) -> None:
        """
        Reverse the affects of the consumable

        :param hero: Hero to affect
        :return: None
        """
        hero.damage -= 1


class PierceShot(ConsumableLoot, ABC):
    DESC = """Guarantee success in combat"""
    NAME = "PierceShot"

    def __init__(self):
        super().__init__(AttackPotion.NAME, AttackPotion.DESC)

    def consume(self, hero: Hero) -> None:
        pass

    def remove_affect(self, hero: Hero) -> None:
        pass

