import unittest
import sys, os

# Legg til src-mappen til sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'Oving_2', 'src')))

from DeckOfCards import DeckOfCards
from HandOfCards import HandOfCards

class TestDeckOfCards(unittest.TestCase):

    def test_deck_creation(self):
        deck = DeckOfCards()
        self.assertEqual(len(deck.cards), 52)  # Sjekker at decket har 52 kort

    def test_deal_hand(self):
        deck = DeckOfCards()
        hand = deck.deal_hand(5)  # Del ut 5 kort
        self.assertEqual(len(hand.cards), 5)  # Sjekker at hånden har 5 kort
        self.assertIsInstance(hand, HandOfCards)  # Sjekker at det er en HandOfCards instans

    def test_deal_hand_invalid(self):
        deck = DeckOfCards()
        with self.assertRaises(ValueError):  # Tester om feil heves for ugyldig antall kort
            deck.deal_hand(0)  # Ugyldig antall kort
        with self.assertRaises(ValueError):  # Tester om feil heves for ugyldig antall kort
            deck.deal_hand(53)  # Ugyldig antall kort

if __name__ == '__main__':
    unittest.main()
