import unittest

from poker.card import Card
from poker.validators import StraightFlushValidator

class StraightFlushValidatorTest(unittest.TestCase):
    def test_determines_there_are_not_five_consecutive_cards_with_the_same_suit(self):
        cards = [
            Card(rank = "6", suit = "Spades"),
            Card(rank = "7", suit = "Spades"),
            Card(rank = "8", suit = "Spades"),
            Card(rank = "9", suit = "Spades"),
            Card(rank = "10", suit = "Diamonds"),
            Card(rank = "King", suit = "Spades"),
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = StraightFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_determines_there_are_five_consecutive_cards_with_the_same_suit(self):
        cards = [
            Card(rank = "6", suit = "Spades"),
            Card(rank = "7", suit = "Spades"),
            Card(rank = "8", suit = "Spades"),
            Card(rank = "9", suit = "Spades"),
            Card(rank = "10", suit = "Spades"),
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = StraightFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_valid_collection_of_cards(self):
        six = Card(rank = "6", suit = "Spades")
        seven = Card(rank = "7", suit = "Spades")
        eight = Card(rank = "8", suit = "Spades")
        nine = Card(rank = "9", suit = "Spades")
        ten = Card(rank = "10", suit = "Spades")

        cards = [
            six,
            seven,
            eight,
            nine,
            ten,
            Card(rank = "King", suit = "Clubs"),
            Card(rank = "Ace", suit = "Diamonds")
        ]

        validator = StraightFlushValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                six,
                seven,
                eight,
                nine,
                ten
            ]
        )

    