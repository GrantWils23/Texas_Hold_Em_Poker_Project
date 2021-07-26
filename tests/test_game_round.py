import unittest
from unittest.mock import MagicMock, call

from poker.game_round import GameRound
from poker.card import Card

class GameRoundTest(unittest.TestCase):
    def setUp(self):
        self.first_two_cards = [
            Card(rank = "2", suit = "Hearts"),
            Card(rank = "6", suit = "Diamonds")
        ]
        
        self.next_two_cards = [
            Card(rank = "3", suit = "Spades"),
            Card(rank = "3", suit = "Clubs")
        ]

        self.flop_cards = [
            Card(rank = "2", suit = "Diamonds"),
            Card(rank = "4", suit = "Hearts"),
            Card(rank = "10", suit = "Spades")
        ]

        self.turn_card = [
            Card(rank = "9", suit = "Hearts")
        ]

        self.river_card = [
            Card(rank = "King", suit = "Clubs")
        ]


    def test_stores_deck_and_players(self):
        deck = MagicMock()

        players = [
            MagicMock(),
            MagicMock()

        ]

        game_round = GameRound(
            deck = deck,
            players = players
        )

        self.assertEqual(
            game_round.deck,
            deck
        )

        self.assertEqual(
            game_round.players,
            players
        )

    def test_game_play_shuffles_deck(self):
        mock_deck = MagicMock()

        players = [
            MagicMock(),
            MagicMock()
        ]

        game_round = GameRound(
           deck = mock_deck,
           players = players 
        )

        game_round.play()

        mock_deck.shuffle.assert_called_once()

    def test_deals_two_initial_cards_to_each_player(self):
        mock_deck = MagicMock()
        mock_deck.remove_cards.side_effect = [
            self.first_two_cards, 
            self.next_two_cards,
            self.flop_cards,
            self.turn_card,
            self.river_card
            ]

        mock_player_1 = MagicMock()
        mock_player_2 = MagicMock()

        players = [mock_player_1, mock_player_2]

        game_round = GameRound(
           deck = mock_deck,
           players = players 
        )

        game_round.play()

        mock_deck.remove_cards.assert_has_calls([
            call(2), call(2)    
        ])

        mock_player_1.add_cards.assert_has_calls([
            call(self.first_two_cards)
        ])

        mock_player_2.add_cards.assert_has_calls([
            call(self.next_two_cards)
        ])

    def test_removes_player_if_not_willing_to_place_bet(self):
        deck = MagicMock()    
        mock_player_1 = MagicMock()
        mock_player_2 = MagicMock()
        players = [mock_player_1, mock_player_2]
        mock_player_1.wants_to_fold.return_value = True
        mock_player_2.wants_to_fold.return_value = False

        game_round = GameRound(deck = deck, players = players)
        game_round.play()
        
        self.assertEqual(
            game_round.players,
            [mock_player_2]
        )


    def test_deals_same_3_flop_1_turn_1_river_cards_to_each_player(self):
        mock_player_1 = MagicMock()
        mock_player_1.wants_to_fold.return_value = False 
        mock_player_2 = MagicMock()
        mock_player_2.wants_to_fold.return_value = False
        players = [mock_player_1, mock_player_2]


        mock_deck = MagicMock()
        mock_deck.remove_cards.side_effect = [
            self.first_two_cards,
            self.next_two_cards,
            self.flop_cards,
            self.turn_card,
            self.river_card
        ]

        game_round = GameRound(deck = mock_deck, players = players)
        game_round.play()

        mock_deck.remove_cards.assert_has_calls(
            [call(3), call(1), call(1)]
            )

        calls = [
            call(self.flop_cards),
            call(self.turn_card),
            call(self.river_card)
        ]

        for player in players:
            player.add_cards.assert_has_calls(calls)




        # mm.fakemethod()

        # mm.fakemethod.call_args_list
