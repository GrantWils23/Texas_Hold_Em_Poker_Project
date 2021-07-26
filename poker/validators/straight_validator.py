from poker.validators import FiveCardRanksInARowValidator

class StraightValidator(FiveCardRanksInARowValidator):
    def __init__(self, cards):
        self.cards = cards
        self.name = "Straight"

    def is_valid(self):
        return len(self._collections_of_five_straight_cards_in_a_row) >= 1

    def valid_cards(self):
        return self._collections_of_five_straight_cards_in_a_row[-1]

#    def is_valid(self):
#         # if len(self.cards) < 5:
#         #     return False            NO LONGER REQUIRED AS 
#                                       NEW CODE SATISFIES THIS
#                                       LOGICAL REQUIREMENT
#                                       WITHIN @Property coding