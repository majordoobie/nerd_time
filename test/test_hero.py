import unittest

from packages.characters.hero import Hero


class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("The Great Kai")

    def test_hero_init(self):
        """Test that a hero can be initialized"""
        self.assertEqual(self.hero.name, "The Great Kai")

        with self.assertRaises(AttributeError):
            self.hero.name = "Sometyhing else"

    def test_number_of_faces(self):
        """Test the die face mechanism for items"""
        self.assertEqual(self.hero.die_faces, 6)
        self.hero.die_faces += 1
        self.assertEqual(self.hero.die_faces, 7)

    def test_number_of_die_count(self):
        """Test the die count mechanism for items"""
        self.assertEqual(self.hero.dice_count, 3)
        self.hero.dice_count += 1
        self.assertEqual(self.hero.dice_count, 4)




if __name__ == '__main__':
    unittest.main()
