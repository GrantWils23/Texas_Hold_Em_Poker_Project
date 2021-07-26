import unittest
from poker.card import Card
from poker.validators import TwoPairValidator

class TwoPairValidatorTest(unittest.TestCase):
    def setUp(self):
        self.three_of_clubs = Card(rank = "3", suit = "Clubs")
        self.three_of_hearts = Card(rank = "3", suit = "Hearts")
        self.nine_of_diamonds = Card(rank = "9", suit = "Diamonds")
        self.nine_of_hearts = Card(rank = "9", suit = "Hearts")
        self.king_of_clubs = Card(rank = "King", suit = "Clubs")

        self.cards = [
            self.three_of_clubs,
            self.three_of_hearts,
            self.nine_of_diamonds,
            self.nine_of_hearts,
            self.king_of_clubs
        ]

    def test_validates_that_cards_have_exactly_two_pair(self):
        validator = TwoPairValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )
        
    def test_returns_two_pair_from_card_collection(self):
        validator = TwoPairValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [   
                self.three_of_clubs, 
                self.three_of_hearts,
                self.nine_of_diamonds,
                self.nine_of_hearts
            ]
        )   