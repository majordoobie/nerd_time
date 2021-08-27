import unittest

from packages.characters.hero import Hero
from packages.environments.consumable_loot import AttackPotion


class TestConsumableLoot(unittest.TestCase):
    def setUp(self) -> None:
        self.hero = Hero("Samurai Jack")

    def test_attack_potion(self):
        potion = AttackPotion()
        self.assertEqual(self.hero.dice_count, 3)
        potion.consume(self.hero)
        self.assertEqual(self.hero.dice_count, 4)
        potion.remove_affect(self.hero)
        self.assertEqual(self.hero.dice_count, 3)

if __name__ == '__main__':
    unittest.main()
