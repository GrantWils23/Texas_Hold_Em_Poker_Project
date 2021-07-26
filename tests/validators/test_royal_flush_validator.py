import unittest

from poker.card import Card
from poker.validators import RoyalFlushValidator

class RoyalFlushValidatorTest(unittest.TestCase):
    def test_determines_there_are_five_consecutive_cards_with_the_same_suit_is_not_a_royal_flush(self):
        cards = [
            Card(rank = "4", suit = "Clubs"),
            Card(rank = "9", suit = "Hearts"),
            Card(rank = "10", suit = "Hearts"),
            Card(rank = "Jack", suit = "Hearts"),
            Card(rank = "Queen", suit = "Hearts"),
            Card(rank = "King", suit = "Hearts"),
            Card(rank = "Ace", suit = "Spades")
        ]

        validator = RoyalFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_determines_there_are_five_consecutive_cards_with_the_same_suit_is_a_royal_flush(self):
        cards = [
            Card(rank = "4", suit = "Clubs"),
            Card(rank = "9", suit = "Spades"),
            Card(rank = "10", suit = "Hearts"),
            Card(rank = "Jack", suit = "Hearts"),
            Card(rank = "Queen", suit = "Hearts"),
            Card(rank = "King", suit = "Hearts"),
            Card(rank = "Ace", suit = "Hearts")
        ]

        validator = RoyalFlushValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
        True
        )
    
    def test_returns_valid_collection_of_cards(self):
        
        ten = Card(rank = "10", suit = "Hearts")
        jack = Card(rank = "Jack", suit = "Hearts")
        queen = Card(rank = "Queen", suit = "Hearts")
        king = Card(rank = "King", suit = "Hearts")
        ace = Card(rank = "Ace", suit = "Hearts")

        cards = [
            Card(rank = "4", suit = "Clubs"),
            Card(rank = "9", suit = "Spades"),
            ten,
            jack,
            queen,
            king,
            ace

        ]

        validator = RoyalFlushValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
        [
            ten,
            jack,
            queen,
            king, 
            ace
        ]
        )
