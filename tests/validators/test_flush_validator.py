import unittest
from poker.card import Card
from poker.validators import FlushValidator

class FlushValidatorTest(unittest.TestCase):
    def setUp(self):
        self.three_of_hearts    = Card(rank = "3", suit = "Hearts")
        self.five_of_hearts     = Card(rank = "5", suit = "Hearts")
        self.nine_of_hearts     = Card(rank = "9", suit = "Hearts")
        self.eight_of_hearts    = Card(rank = "8", suit = "Hearts")
        self.jack_of_hearts     = Card(rank = "Jack", suit = "Hearts")
        self.ace_of_hearts      = Card(rank = "Ace", suit = "Hearts")

        self.cards = [
            self.three_of_hearts,
            self.five_of_hearts,
            self.eight_of_hearts,
            self.nine_of_hearts,
            self.jack_of_hearts,
            Card(rank = "Jack", suit = "Spades"),
            self.ace_of_hearts
        ]

    def test_validates_that_five_cards_of_the_same_suit_exist_in_the_same_collection(self):
        validator = FlushValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_the_five_highest_cards_with_the_same_suit(self):
        validator = FlushValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.five_of_hearts,
                self.eight_of_hearts,
                self.nine_of_hearts,
                self.jack_of_hearts,
                self.ace_of_hearts
            ]
        )