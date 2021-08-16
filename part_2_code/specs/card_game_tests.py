import unittest
from src.card import Card
from src.card_game import *

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Clubs", 1)
        self.card2 = Card("Hearts", 10)
        self.cards = [self.card1, self.card2]

    def test_check_for_ace(self):
        self.assertEqual(True, check_for_ace(self.card1))

    def test_check_high_card(self):
        self.assertEqual(self.card2, highest_card(self.card1, self.card2))

    def test_total(self):
        self.assertEqual("You have a total of 11", cards_total(self.cards))