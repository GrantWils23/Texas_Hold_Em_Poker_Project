class SuitValidator():
    def _suits_occurrence_count(self, count):
        return {
            suit: suit_count
            for suit, suit_count in self._card_suit_counts.items()
            if suit_count == count
        }

    @property
    def _card_suit_counts(self):
        card_suit_counts = {}
        for card in self.cards:
            card_suit_counts.setdefault(card.suit, 0)
            card_suit_counts[card.suit] += 1
        return card_suit_counts
