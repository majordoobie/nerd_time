import unittest

from packages.environments.environment import Environment, InitiativeEnum


class TestEnvironment(unittest.TestCase):
    def setUp(self) -> None:
        self.spooky = Environment("Spooky Place", "Very Spooky Place", 1, None)

    def test_env_init(self):
        """Test to make sure we can init the class"""
        self.assertIsInstance(self.spooky, Environment)

    def test_initiative(self):
        """Test to make sure we get a Enum type as a return"""
        self.assertIsInstance(self.spooky.initiative(), InitiativeEnum)
        enum = self.spooky.initiative()
        self.assertTrue((enum == InitiativeEnum.HERO) or (enum == InitiativeEnum.MONSTER))


if __name__ == '__main__':
    unittest.main()
