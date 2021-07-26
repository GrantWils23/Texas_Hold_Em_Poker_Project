import unittest
from poker.card import Card
from poker.validators import PairValidator

class PairValidatorTest(unittest.TestCase):
    def test_validates_that_cards_have_exactly_one_pair(self):
        cards = [
            Card(rank = "Jack", suit = "Clubs"),
            Card(rank = "Jack", suit = "Spades")
        ]

        validator = PairValidator(cards = cards)

        self.assertEqual(
            validator.is_valid(),
            True
            )

        
    def test_returns_pair_from_card_collection(self):
        jack_of_diamonds = Card(rank = "Jack", suit = "Diamonds")
        jack_of_hearts = Card(rank = "Jack", suit = "Hearts")

        cards = [
            Card(rank = "5", suit = "Spades"),
            Card(rank = "8", suit = "Diamonds"),
            jack_of_diamonds,
            jack_of_hearts,
            Card(rank = "King", suit = "Clubs"),
        ]

        validator = PairValidator(cards = cards)

        self.assertEqual(
            validator.valid_cards(),
            [jack_of_diamonds, jack_of_hearts])