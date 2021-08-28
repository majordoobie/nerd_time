import unittest

from packages.environments.environment import Environment, InitiativeEnum
from packages.environments.consumable_loot import LuckySeven, AttackPotion


class TestEnvironment(unittest.TestCase):
    def setUp(self) -> None:
        self.spooky = Environment("Spooky Place", "Very Spooky Place", 1, None)
        self.attack_potion = AttackPotion()
        self.lucky_seven = LuckySeven()

    def test_env_init(self):
        """Test to make sure we can init the class"""
        self.assertIsInstance(self.spooky, Environment)

    def test_initiative(self):
        """Test to make sure we get a Enum type as a return"""
        self.assertIsInstance(self.spooky.initiative, InitiativeEnum)
        enum = self.spooky.initiative
        self.assertTrue((enum == InitiativeEnum.HERO) or (enum == InitiativeEnum.MONSTER))

    def test_loot_mechanism(self):
        self.assertEqual(len(self.spooky.loot), 0)
        self.spooky.add_loot(self.lucky_seven)
        self.assertEqual(len(self.spooky.loot), 1)
        self.spooky.add_loot(self.attack_potion)
        self.assertEqual(len(self.spooky.loot), 2)
        self.spooky.loot_room()
        self.assertEqual(len(self.spooky.loot), 0)






if __name__ == '__main__':
    unittest.main()
