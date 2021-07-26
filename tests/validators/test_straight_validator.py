import unittest
from poker.card import Card
from poker.validators import StraightValidator

class StraightValidatorTest(unittest.TestCase):
    def setUp(self):
            three       = Card(rank = "3", suit = "Hearts")
            self.four   = Card(rank = "4", suit = "Spades")
            self.five   = Card(rank = "5", suit = "Clubs")
            self.six    = Card(rank = "6", suit = "Clubs")
            self.seven  = Card(rank = "7", suit = "Hearts")
            self.eight  = Card(rank = "8", suit = "Diamonds")
            queen       = Card(rank = "Queen", suit = "Diamonds")

            self.cards = [
                three,
                self.four, 
                self.five,
                self.six, 
                self.seven, 
                self.eight, 
                queen
            ]


    def test_determines_if_there_are_five_cards_in_a_row(self):
        validator = StraightValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_does_not_deem_two_consecutive_cards_as_straight(self):
        cards = [
            Card(rank = "6", suit = "Hearts"),
            Card(rank = "7", suit = "Diamonds")
        ]

        validator = StraightValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_returns_five_highest_cards_in_a_row(self):
        validator = StraightValidator(cards = self.cards)

        self.assertEqual(validator.valid_cards(),
            [
            self.four,
            self.five,
            self.six,
            self.seven,
            self.eight
            ]
        )
