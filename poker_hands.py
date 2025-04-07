from itertools import pairwise

# List out the hand categories
hand_categories = ('High Card',
                   'Pair',
                   'Two Pair',
                   'Three of a Kind',
                   'Straight',
                   'Flush',
                   'Full House',
                   'Four of a Kind',
                   'Straight Flush',
                   'Royal Flush')
def is_royal_flush(hand):
    """
    Check if hand contains royal flush. 
    Returns: True and hand, or False and None
    rtype: tuple(bool, list(Card))
    """
    hand.sort(reverse=True)
    royal_hand = is_straight_flush(hand)[0] \
                and hand[0].rank == 'A' \
                and hand[-1].rank == '10'
    if royal_hand:
        return True, hand
    return False, None

def is_straight_flush(hand):
    """
    Check if hand contains a straight flush.
    Returns: True and hand, or False and None
    rtype: tuple(bool, list(Card))
    """
    hand.sort(reverse=True)
    st_flush = is_flush(hand)[0] and is_straight(hand)[0]

    if st_flush:
        return True, hand
    return False, None

def is_flush(hand):
    """
    Checks if hand contains a flush.
    Returns: True and hand, or False and None
    rtype: Tuple(bool, Optional[List[Card]])
    """
    hand.sort(reverse=True)
    suites_in_hand = set(card.suit for card in hand)
    if len(suites_in_hand) == 1:
        return True, hand
    return False, None

def is_straight(hand):
    """
    Check if hand contains a straight."""

    hand.sort(reverse=True)
    if hand[0].rank == 'A' and hand[1].rank.isdigit():
        # If ace is present and other cards are digits then treat ace as 1
        hand = hand[1:] + hand[0:1]
    for i in range(0, len(hand), 2):
        if hand[i] - hand[i+1] != 1:
            return False, None
    
    return True, hand

def is_four_of_a_kind(hand):
    """
    Checks hand for four of a kind.
    """
    hand.sort(reverse=True)
    ranks_in_hand = set(card.rank for card in hand)
    if len(ranks_in_hand) == 1:
        return True, hand
    return False, None

def is_full_house(hand):
    """
    Checks if a hand is a full house.
    """
    hand.sort(reverse=True)
    is_tres, tres = is_three_of_a_kind(hand)
    if is_tres:
        other_cards = [card for card in hand if card not in tres]
        if is_pair(other_cards):
            return True, hand
    
    return False, None

def is_three_of_a_kind(hand):
    hand.sort(reverse=True)
    # Check triplets being equal

    for i in range(3):
        if hand[i].rank == hand[i + 1].rank == hand[i+2].rank:
            return True, hand[i: i+3]
        
    return False, None

def is_two_pair(hand):
    two_pairs = []
    list_pairs = list(pairwise(hand))
    skip_next = False
    for c1,c2 in list_pairs:
        if skip_next:
            skip_next = False
        elif c1.rank == c2.rank:
            two_pairs.extend([c1, c2])
            skip_next = True
    
    if len(two_pairs) == 4:
        return True, two_pairs
    return False, None

def is_pair(hand):
    hand.sort(reverse = True)
    found = False
    pair_idx = -1
    for i in range(len(hand) - 1):
        if not found and hand[i].rank == hand[i+1].rank:
            found = True
            pair_idx = i
        elif found and hand[i].rank == hand[i + 1].rank:
            raise Exception('More than one pair found after two pair check. Correct code!')
    if found:
        return True, hand[pair_idx: pair_idx + 2]
    
    return False, None
    
    return hand[pair_idx: pair_idx + 2]
def is_high_card(hand):
    hand.sort(reverse=True)
    return True, hand[0]