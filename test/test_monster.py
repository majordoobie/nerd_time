import unittest

from packages.characters.monster import Monster


class TestMonster(unittest.TestCase):
    def setUp(self) -> None:
        self.imp = Monster("Imp", 1, 3)
        self.wraith = Monster("Wraith", 3, 3)

    def test_monster_init(self):
        """Test Hierarchy """
        self.assertEqual(f"{self.imp.__class__.__name__}: {self.imp.name}", "Monster: Imp")

    def test_monster_combat_dice(self):
        """Test the creation of a monster that the dice count returned"""
        combat_rolls = self.imp.combat_roll()
        self.assertEqual(len(combat_rolls), self.imp.dice_count)

    def test_read_only(self):
        """Make sure that data is protected"""
        with self.assertRaises(AttributeError):
            self.imp.name = "Stuff"

    def test_damage_taken(self):
        """Test that health is decremented and death is triggered"""
        self.assertEqual(self.imp.health, 1)
        self.assertFalse(self.imp.is_dead)
        self.imp.takes_hit()
        self.assertTrue(self.imp.is_dead)


if __name__ == '__main__':
    unittest.main()
