import unittest

from poker.card import Card
from poker.validators import FourOfAKindValidator

class FourOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        self.king_of_clubs      = Card(rank = "King", suit = "Clubs")
        self.king_of_spades     = Card(rank = "King", suit = "Spades")
        self.king_of_hearts     = Card(rank = "King", suit = "Hearts")
        self.king_of_diamonds   = Card(rank = "King", suit = "Diamonds")

        self.cards = [
            Card(rank = "6", suit = "Clubs"),
            Card(rank = "7", suit = "Clubs"),
            Card(rank = "10", suit = "Spades"),
            self.king_of_clubs,
            self.king_of_diamonds,
            self.king_of_hearts,
            self.king_of_spades
        ]

    def test_validates_four_of_a_kind_cards(self):
        validator = FourOfAKindValidator(cards = self.cards)

        self.assertEqual(validator.is_valid(),
        True
        )

    def test_returns_four_of_a_kind_from_card_collection(self):
        validator = FourOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.king_of_clubs,
                self.king_of_diamonds,
                self.king_of_hearts,
                self.king_of_spades
            ]
        )