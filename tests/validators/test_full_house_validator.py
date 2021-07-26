import unittest
from poker.card import Card
from poker.validators import FullHouseValidator

class FullHouseValidatorTest(unittest.TestCase):
    def setUp(self):
        self.three_of_clubs     = Card(rank = "3", suit = "Clubs")
        self.three_of_spades    = Card(rank = "3", suit = "Spades")
        self.three_of_hearts    = Card(rank = "3", suit = "Hearts")
        self.six_of_diamonds    = Card(rank = "6", suit = "Diamonds")
        self.six_of_clubs       = Card(rank = "6", suit = "Clubs")
    
        self.cards = [
            self.three_of_clubs,
            self.three_of_hearts,
            self.three_of_spades,
            self.six_of_clubs,
            self.six_of_diamonds
        ]

    def test_validates_the_cards_are_a_full_house(self):
        validator = FullHouseValidator(cards = self.cards)

        self.assertEqual(validator.is_valid(),
        True
        )

    def test_returns_full_house_cards_from_card_collection(self):
        validator = FullHouseValidator(cards = self.cards)

        self.assertEqual(validator.valid_cards(),
        [
            self.three_of_clubs,
            self.three_of_hearts,
            self.three_of_spades,
            self.six_of_clubs,
            self.six_of_diamonds
        ]
        )