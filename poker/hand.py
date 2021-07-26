from poker.validators import (
    NoCardValidator,
    HighCardValidator,
    PairValidator,
    TwoPairValidator,
    ThreeOfAKindValidator,
    StraightValidator,
    FlushValidator,
    FullHouseValidator,
    FourOfAKindValidator,
    StraightFlushValidator,
    RoyalFlushValidator
)

class Hand():
    VALIDATORS = (                  # Class Attribute (accessible across every instance)
        RoyalFlushValidator,
        StraightFlushValidator,
        FourOfAKindValidator,
        FullHouseValidator,
        FlushValidator,
        StraightValidator,
        ThreeOfAKindValidator,
        TwoPairValidator,
        PairValidator,
        HighCardValidator,
        NoCardValidator
    )


    def __init__(self):
        self.cards = []
    
    def __repr__(self):
        cards_as_strings = [str(card) for card in self.cards]
        return ", ".join(cards_as_strings)

    def add_cards(self, cards):
        copy = self.cards[:]
        copy.extend(cards)
        copy.sort()
        self.cards = copy

    def best_rank(self):
        for index, validator_klass in enumerate(self.VALIDATORS):
            validator = validator_klass(cards = self.cards)
            if validator.is_valid():
                return (index, validator.name, validator.valid_cards())

    

    # @property                                         # Instance Attribute
    # def _rank_validations_from_best_to_worst(self):
    #     return (
    #         ("Royal Flush", RoyalFlushValidator(cards =self.cards).is_valid),
    #         ("Straight Flush", StraightFlushValidator(cards = self.cards).is_valid),
    #         ("Four of a Kind", FourOfAKindValidator(cards= self.cards).is_valid),
    #         ("Full House", FullHouseValidator(cards = self.cards).is_valid),
    #         ("Flush", FlushValidator(cards = self.cards).is_valid),
    #         ("Straight", StraightValidator(cards = self.cards).is_valid),
    #         ("Three of a Kind", ThreeOfAKindValidator(cards = self.cards).is_valid),
    #         ("Two Pair", TwoPairValidator(cards = self.cards).is_valid),
    #         ("Pair", PairValidator(cards = self.cards).is_valid),
    #         ("High Card", HighCardValidator(cards = self.cards).is_valid),
    #         ("No Cards", NoCardValidator(cards = self.cards).is_valid)
    #     )
