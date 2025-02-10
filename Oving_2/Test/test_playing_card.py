import unittest
import sys, os

# Legg til src-mappen til sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'Oving_2', 'src')))

from PlayingCard import PlayingCard

class TestPlayingCard(unittest.TestCase):

    def test_card_creation(self):
        card = PlayingCard('H', 5)
        self.assertEqual(card.get_suit(), 'H')
        self.assertEqual(card.get_face(), 5)

    def test_invalid_suit(self):
        with self.assertRaises(ValueError):
            PlayingCard('X', 5)

    def test_invalid_face(self):
        with self.assertRaises(ValueError):
            PlayingCard('H', 15)

    def test_get_as_string(self):
        card = PlayingCard('D', 10)
        self.assertEqual(card.get_as_string(), 'D10')

if __name__ == '__main__':
    unittest.main()
