from unittest import TestCase

from packages.characters.hero import Hero
from packages.characters.monster import Monster
from packages.game_utils.combat_functions import duel
from packages.environments.consumable_loot import HeavyHand, PierceShot


class TestDuel(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Samurai Jack")
        self.monster = Monster("Imp", 3, 1)
        self.heavy_hand = HeavyHand()
        self.pierce_shot = PierceShot()

    def test_duel(self):
        """Test that combat is functioning properly"""
        self.hero._combat_rolls = [6, 6, 3]
        self.monster._combat_rolls = [3]

        self.assertEqual(self.monster.health, 3)
        self.assertTrue(duel(self.hero, self.monster, debug=True))
        self.assertEqual(self.monster.health, 2)

    def test_with_potions(self):
        """Test that multiple potions still result in expected damage to monster"""

        # set increase damage and guarantee hit
        self.heavy_hand.consume(self.hero)
        self.pierce_shot.consume(self.hero)

        self.hero.combat_roll()

        # make sure we have all six
        for die in self.hero.combat_rolls:
            self.assertEqual(die, 6)

        self.monster._combat_rolls = [3]

        self.assertEqual(self.monster.health, 3)
        self.assertTrue(duel(self.hero, self.monster, debug=True))
        self.assertEqual(self.monster.health, 1)

    def test_fail_attack(self):
        """Test a hero failing a attack"""
        self.hero.combat_roll()
        self.monster._combat_rolls = [6]

        self.assertEqual(self.monster.health, 3)
        self.assertFalse(duel(self.hero, self.monster, debug=True))
        self.assertEqual(self.monster.health, 3)


