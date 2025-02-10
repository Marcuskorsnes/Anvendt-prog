import unittest
import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'Oving_2', 'src')))

from HandOfCards import HandOfCards
from PlayingCard import PlayingCard

class TestHandOfCards(unittest.TestCase):

    def test_is_flush(self):
        cards = [PlayingCard('H', 1), PlayingCard('H', 2), PlayingCard('H', 3), PlayingCard('H', 4), PlayingCard('H', 5)]
        hand = HandOfCards(cards)
        self.assertTrue(hand.is_flush())

    def test_is_not_flush(self):
        cards = [PlayingCard('H', 1), PlayingCard('D', 2), PlayingCard('H', 3), PlayingCard('H', 4), PlayingCard('S', 5)]
        hand = HandOfCards(cards)
        self.assertFalse(hand.is_flush())

    def test_str(self):
        cards = [PlayingCard('H', 1), PlayingCard('H', 2), PlayingCard('H', 3)]
        hand = HandOfCards(cards)
        self.assertEqual(str(hand), 'H1, H2, H3')

if __name__ == '__main__':
    unittest.main()
