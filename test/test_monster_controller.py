from unittest import TestCase

from packages.game_utils.monster_controller import MonsterController, EnvironmentRecord
from packages.environments.environment import Environment


class TestMonsterController(TestCase):
    def setUp(self) -> None:
        self.env1 = Environment("Cave", "Scary", 1, ["Imp", "Mad Cow"])
        self.env2 = Environment("Cave", "Scary", 5)

    def test_monster_one_count(self):
        """Test creating of 1 monster"""
        monster_controller = MonsterController(EnvironmentRecord(self.env1.level, self.env1.habitable))
        self.assertEqual(monster_controller.monster_count, 1)

    def test_monster_multi_count(self):
        """Increment level and get monster count"""
        monster_controller = MonsterController(EnvironmentRecord(self.env2.level, self.env2.habitable))
        self.assertEqual(monster_controller.monster_count, 3)

    def test_monster_deaths(self):
        """Test if the monsters are popped from the list"""
        monster_controller = MonsterController(EnvironmentRecord(self.env2.level, self.env2.habitable))
        self.assertEqual(monster_controller.monster_count, 3)

        monster_controller.monsters[0].is_dead = True
        monster_controller.monsters[2].is_dead = True
        monster_controller.clean_up()
        self.assertEqual(monster_controller.monster_count, 1)
        self.assertEqual(len(monster_controller.monsters), 1)




