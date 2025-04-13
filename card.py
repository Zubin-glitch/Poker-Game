class Card:
    static_ranks = [str(n) for n in range(2, 11)] + ['J', 'Q', 'K', 'A']
    static_suites = ["club", "diamond", "heart", "spade"]
    # Added for testing purposes, TODO: Remove global_deck
    global_deck = []

    # Constructor of the class
    def __init__(self, rank: str, suit: str):
        # Check validity of the rank and suit
        assert rank.upper() in Card.static_ranks, f"{rank} Rank is not valid! Valid ranks are: {Card.static_ranks}"
        assert suit.lower() in Card.static_suites, f"{suit} Suite isn't valid! It should be: {Card.static_suites}"
        
        # Card has two fields
        self.rank = rank.upper()
        self.suit = suit.lower()
        
        # Add card to global list of all instances
        Card.global_deck.append(self)
    
    # Some methods to order the cards
    def __sub__(self, other):
        """
        Returns current card's rank minus another card's rank.
        If current card has higher rank, returns a +ve integer
        Else, other card has higher rank, return a -ve integer
        """
        if self.rank == 'A' and other.rank == '2':
            return 1
        elif self.rank == '2' and other.rank == 'A':
            return -1
        else:
            return Card.static_ranks.index(self.rank) - Card.static_ranks.index(other.rank)
    
    def __lt__(self, other) -> bool:
        return Card.static_ranks.index(self.rank) < Card.static_ranks.index(other.rank)
    
    def __le__(self, other) -> bool:
        return Card.static_ranks.index(self.rank) <= Card.static_ranks.index(other.rank)
    
    def __gt__(self, other) -> bool:
        return Card.static_ranks.index(self.rank) > Card.static_ranks.index(other.rank)
    
    def __ge__(self, other) -> bool:
        return Card.static_ranks.index(self.rank) >= Card.static_ranks.index(other.rank)
    
    def __eq__(self, other) -> bool:
        return Card.static_ranks.index(self.rank) == Card.static_ranks.index(other.rank)
    


    def __str__(self):
        """
        Returns: String representation of the card
        """
        view_card = f"{self.rank}"
        match self.suit:
            case "club":
                view_card += '\u2663'
            case "diamond":
                view_card += '\u2666'
            case "heart":
                view_card += '\u2665'
            case "spade":
                view_card += '\u2660'
            case _:
                raise ValueError("Invalid card suite!")
        return view_card

    def __repr__(self):
        """
        Returns a string that can be used to recreate the object.
        This is the same as str(self).
        """
        return str(self)
    
    def compare(self, other):
        """
        This function compares two cards.
        Returns : 1 (first card is higher in rank than second)
        Returns : 0 (first card and second card have same rank)
        Returns : -1 (first card is lower than second in rank)
        """
        if self > other:
            return 1
        elif self == other:
            return 0
        else:
            return -1

# Unit tests
# card1 = Card('J', 'club')
# print(card1)

# card2 = Card('a', 'heart')
# print(card2)

# card3 = Card('A', 'spade')

# print(card1 - card2)
# print(card2.compare(card1))
# print(card1.compare(card2))
# print(card2.compare(card3))
# print(Card.global_deck)