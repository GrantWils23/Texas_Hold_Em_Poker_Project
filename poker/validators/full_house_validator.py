from poker.validators import RankValidator

class FullHouseValidator(RankValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Full House"

    def is_valid(self):
        ranks_with_three_of_a_kind = self._ranks_with_count(3)
        ranks_with_pairs = self._ranks_with_count(2)
        return len(ranks_with_three_of_a_kind) == 1 and len(ranks_with_pairs) == 1

    def valid_cards(self):
        ranks_with_three_of_a_kind = self._ranks_with_count(3)
        t_o_a_k_cards = [card for card in self.cards if card.rank in ranks_with_three_of_a_kind.keys()]

        ranks_with_pairs = self._ranks_with_count(2)
        pair_cards = [card for card in self.cards if card.rank in ranks_with_pairs.keys()]
        
        all_cards = t_o_a_k_cards + pair_cards
        all_cards.sort()
        return all_cards