import unittest
import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'src')))

from DeckOfCards import DeckOfCards
from PlayingCard import PlayingCard

class TestDeckOfCards(unittest.TestCase):

    def test_deck_creation(self):
        deck = DeckOfCards()
        self.assertEqual(len(deck.cards), 52)

    def test_shuffle_deck(self):
        deck = DeckOfCards()
        original_deck = deck.cards.copy()
        deck.shuffle()
        self.assertNotEqual(deck.cards, original_deck)

    def test_deal_card(self):
        deck = DeckOfCards()
        card = deck.deal_card()
        self.assertEqual(len(deck.cards), 51)
        self.assertIsInstance(card, PlayingCard)

if __name__ == '__main__':
    unittest.main()
