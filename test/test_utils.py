import unittest
from packages.game_utils import utils


class TestUtils(unittest.TestCase):
    def test_utils_roll_dice(self):
        """Test that value error is raised when given a side less than 1 and that only
        an integer is returned"""
        with self.assertRaises(ValueError):
            utils.roll_dice(0)

        self.assertIsInstance(utils.roll_dice(), int)


if __name__ == '__main__':
    unittest.main(verbosity=2)
