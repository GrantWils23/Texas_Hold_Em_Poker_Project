import unittest
from poker.card import Card
from poker.hand import Hand
from poker.validators import PairValidator

class TestHand(unittest.TestCase):
    def test_starts_out_with_no_cards(self):
        hand = Hand()
        self.assertEqual(hand.cards, [])

    def test_shows_all_its_cards_in_technical_representation(self):
        cards = [
            Card(rank = "8", suit = "Clubs"),
            Card(rank = "5", suit = "Hearts")
        ]

        hand = Hand()
        hand.add_cards(cards)
        
        self.assertEqual(
            repr(hand), "5 of Hearts, 8 of Clubs"
        )

    def test_recieves_and_stores_cards(self):
        ace_of_spades = Card(rank = "Ace", suit = "Spades")
        six_of_clubs = Card(rank = "6", suit = "Clubs")

        cards = [
            ace_of_spades,
            six_of_clubs
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.cards, 
            [
                six_of_clubs,
                ace_of_spades
            ]
        )
        
    def test_interacts_with_validator_to_get_winning_hand(self):
        class HandWithOneValidator(Hand):
            VALIDATORS = (PairValidator, ) #Tuple of one element ',' is needed, the () doesn't instanciate a tuple

        ace_of_hearts = Card(rank = "Ace", suit = "Hearts")
        ace_of_spades = Card(rank = "Ace", suit = "Spades")
        cards = [ace_of_hearts, ace_of_spades]

        hand = HandWithOneValidator()
        hand.add_cards(cards = cards)

        self.assertEqual(
            hand.best_rank(),
            (0, "Pair", [ace_of_hearts, ace_of_spades])
        )