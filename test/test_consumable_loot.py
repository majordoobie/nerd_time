import unittest

from packages.characters.hero import Hero
from packages.environments.consumable_loot import AttackPotion, LuckySeven, HealthPotion, HeavyHand, PierceShot


class TestConsumableLoot(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Samurai Jack")

    def test_attack_potion(self):
        """test that dice count increased by 1"""
        potion = AttackPotion()
        self.assertEqual(self.hero.dice_count, 3)
        potion.consume(self.hero)
        self.assertEqual(self.hero.dice_count, 4)
        potion.remove_affect(self.hero)
        self.assertEqual(self.hero.dice_count, 3)

    def test_lucky_seven(self):
        """test that face increased by a factor of 2"""
        potion = LuckySeven()
        self.assertEqual(self.hero.die_faces, 6)
        potion.consume(self.hero)
        self.assertEqual(self.hero.die_faces, 12)
        potion.remove_affect(self.hero)
        self.assertEqual(self.hero.die_faces, 6)

    def test_health_potion(self):
        """Test that health potions increment health correctly"""
        potion = HealthPotion()
        self.assertEqual(self.hero.health, 10)
        potion.consume(self.hero)
        self.assertEqual(self.hero.health, 10)
        self.hero.health -= 5
        potion.consume(self.hero)
        self.assertEqual(self.hero.health, 8)
        potion.remove_affect(self.hero)

    def test_heavy_hand(self):
        """Test that damage is increased from heavy hand potion"""
        potion = HeavyHand()
        self.assertEqual(self.hero.damage, 1)
        potion.consume(self.hero)
        self.assertEqual(self.hero.damage, 2)
        potion.remove_affect(self.hero)
        self.assertEqual(self.hero.damage, 1)

    def test_pierce_shot(self):
        """Test that pierce shot buff is enabled with potion"""
        potion = PierceShot()
        self.assertFalse(self.hero.pierce_shot)
        potion.consume(self.hero)
        self.assertTrue(self.hero.pierce_shot)
        potion.remove_affect(self.hero)
        self.assertFalse(self.hero.pierce_shot)


if __name__ == '__main__':
    unittest.main()
