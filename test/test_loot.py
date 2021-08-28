from unittest import TestCase

from packages.environments.loot import Loot


class TestLoot(TestCase):
    def setUp(self) -> None:
        self.loot = Loot("schmeckle", "RIck and Morty Currency")

    def test_sensitive(self):
        """Test that the object cannot be modified more than we exped"""
        with self.assertRaises(AttributeError):
            self.loot.name = "USD"

        with self.assertRaises(AttributeError):
            self.loot.exists = True

    def test_add_qty(self):
        """Test that the exist is flipped"""
        self.assertTrue(self.loot.exists)
        self.loot.add_qty()
        self.assertTrue(self.loot.exists)

    def test_decrement_qty(self):
        """Test that we cannot decrement beyond "not existing" """
        self.assertTrue(self.loot.exists)
        self.loot.decrement_qty()

        with self.assertRaises(ValueError):
            self.loot.decrement_qty()

    def test_add_decrement_qty(self):
        """Confirm that we can bounce in and out of existence"""
        self.assertTrue(self.loot.exists)
        self.loot.decrement_qty()
        self.assertFalse(self.loot.exists)



