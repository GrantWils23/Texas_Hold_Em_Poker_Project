import unittest
from poker.card import Card
from poker.validators import NoCardValidator

class NoCardValidatorTest(unittest.TestCase):
    def test_validates_player_has_no_cards(self):
        cards = []

        validator = NoCardValidator(cards = cards)

        self.assertEqual(validator.is_valid(),
        True
        )

    def returns_no_cards_from_collection(self):
        cards = []

        validator = NoCardValidator(cards = cards)

        self.assertEqual(validator.is_valid(),
        []
        )