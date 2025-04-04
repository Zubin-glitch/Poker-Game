class Card:
    valid_ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    valid_suits = ["club", "diamond", "heart", "spade"]
    global_deck = []
    # Constructor of the class
    def __init__(self, rank: str, suit: str):
        # Check validity of the rank and suit
        assert rank.upper() in Card.valid_ranks, f"{rank} Rank is not valid! Valid ranks are: {Card.valid_ranks}"
        assert suit.lower() in Card.valid_suits, f"{suit} Suit isn't valid! It should be: {Card.valid_suits}"
        
        # Card has two fields
        self.rank = rank.upper()
        self.suit = suit.lower()
        
        # Add card to global list of all instances
        Card.global_deck.append(self)
    
    def __lt__(self, card):
        pass
    def get_rank(self):
        return self.rank
    
    def get_suit(self):
        return self.suit

    def __str__(self):
        return f"Card({self.rank} {self.suit})"

    def __repr__(self):
        return f"({self.rank}, {self.suit})"

# card1 = Card('J', 'club')
# print(card1)

# card2 = Card('a', 'heart')
# print(card2)

# print(Card.global_deck)