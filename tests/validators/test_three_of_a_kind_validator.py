import unittest
from poker.card import Card
from poker.validators import ThreeOfAKindValidator

class ThreeOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        two_of_hearts = Card(rank = "2", suit = "Hearts")
        four_of_hearts = Card(rank = "4", suit = "Hearts")
        self.jack_of_clubs = Card(rank = "Jack", suit = "Clubs")
        self.jack_of_diamonds = Card(rank = "Jack", suit = "Diamonds")
        self.jack_of_spades = Card(rank = "Jack", suit = "Spades")
        
        self.cards = [
            two_of_hearts,
            four_of_hearts,
            self.jack_of_clubs,
            self.jack_of_diamonds,
            self.jack_of_spades
        ]

    def test_validates_player_has_exactly_three_of_a_kind(self):
        validator = ThreeOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_three_of_a_kind_from_card_collection(self):
        validator = ThreeOfAKindValidator(cards = self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [   
                self.jack_of_clubs,
                self.jack_of_diamonds,
                self.jack_of_spades
            ]
        )
