from poker_hands import *
from card import Card

category_funcs = (is_royal_flush,
                  is_straight_flush,
                  is_four_of_a_kind,
                  is_full_house,
                  is_flush,
                  is_straight,
                  is_three_of_a_kind,
                  is_two_pair,
                  is_pair,
                  is_high_card
                  )

def compute_best_hand(hands_list):
    """
    Given a list of poker hands, return the best hand.
    Returns: best hand in the i/p list.
    rtype: List[Card]
    """
    # Base Case: Leaf/LeafParent node worker
    if len(hands_list) < 2:
        return hands_list[0]
    elif len(hands_list) == 2:
        match compare_hands(hands_list[0], hands_list[1]):
            case 0:
                # both hands are tied
                return hands_list[0]
            case 1:
                return hands_list[0]
            case -1:
                return hands_list[1]
    
    # Recursive Case: Internal node worker
    # divide list into two equal halves and recursively call best_hand on each half
    left = compute_best_hand(hands_list[0: len(hands_list // 2)])
    right = compute_best_hand(hands_list[len(hands_list) // 2: ])
    return compute_best_hand([left, right])

def compare_hands(hand1, hand2):
    """
    Poker hand is a collection of 5 cards.
    Compare two hands to determine which one
    is better. 
    params: hand1, hand2
    return: which hand is better(tie = 0, hand1 = 1, hand2 = -1)
    rtype: int"""
    
    global hand_categories
    h1_category = categorize_hand(hand1)
    h2_category = categorize_hand(hand2)

    if hand_categories.index(h1_category) < hand_categories.index(h2_category):
        return -1
    elif hand_categories.index(h1_category) > hand_categories.index(h2_category):
        return 1
    else:
        # both hands fall in the same category
        if h1_category == 'Royal Flush':
            # it is the highest category with a particular combination
            # if two hands have the same category, it must be a tie.
            return 0
        
        elif h1_category == 'Straight Flush' or h1_category =='Flush' or h1_category == 'Straight':
            # in these categories when the cards are already sorted,
            # we just need to find the highest card which differentiates
            # the two hands
            return hand1[0].compare(hand2[0])
        
        elif h1_category == 'Four of a Kind':
            # for this category we find the kicker
            # which is the highest card with a 4 of a kind comparison
            # check the quad ranks and then kicker to break ties.
            # The second card must be part of the quad.
            # Question: Can there be two quads?
            # Answer: Not in standard poker, but think about what happens
            # if a wildcard is introduced.
            quad_comp = hand1[1].compare(hand2[1])
            if quad_comp == 0:
                # quad ranks are tied, compare kickers
                if hand1[0].compare(hand1[1]) == 0:
                    # kicker is the last card
                    return hand1[-1].compare(hand2[-1])
                else:
                    # kicker is the first card
                    return hand1[0].compare(hand2[0])
            return quad_comp
        
        elif h1_category == 'Full House':
            # need two comparisons, first compare the tres rank
            # then compare the pair rank if tie is not broken,
            # the result is returned.
            # of the 5 cards, the third card must be part of the tres
            tres_comp = hand1[2].compare(hand2[2])
            if tres_comp == 0:
                # tres is a tie
                if hand1[1].compare(hand1[2]) == 0:
                    # triple is in first half
                    return hand1[-1].compare[hand2[-1]]
                else:
                    # triple is in the second half
                    return hand1[0].compare(hand2[0])
            return tres_comp

        elif h1_category == 'Three of a Kind':
            # compare tres rank and if it's a tie compare kicker
            # Again, third card is always part of the tres
            # tres_comp = hand1[2].compare(hand2[2])
            # --------This approach has a bug--------
            # if tres_comp == 0:
            #     if hand1[1].compare(hand1[2]) == 0:
            #         # triple is in first half
            #         return hand1[-2].compare(hand2[-2])
            #     else:
            #         # triple is in second half
            #         return hand1[0].compare(hand2[0])
            # return tres_comp
            _, h1_tres = is_three_of_a_kind(hand1)
            _, h2_tres = is_three_of_a_kind(hand2)
            if h1_tres[0].rank == h2_tres[0].rank:
                # Tied triples, find the kickers
                search_rank = h1_tres[0].rank
                h1_kickers = []
                h2_kickers = []
                for i in range(len(hand1)):
                    if hand1[i].rank != search_rank:
                        h1_kickers.append(hand1[i])
                    if hand2[i].rank != search_rank:
                        h2_kickers.append(hand2[i])
                
                for c1, c2 in zip(h1_kickers, h2_kickers):
                    cmp = c1.compare(c2)
                    if cmp != 0:
                        return cmp
                return 0 # all the same ranked cards
            return h1_tres[0].compare(h2_tres[0])
        
        elif h1_category == 'Two Pair':
            # Compare two pairs
            first_pair_cmp = hand1[1].compare(hand2[1])
            if first_pair_cmp == 0:
                # tie in the first pair
                return hand1[-2].compare(hand2[-2])
            return first_pair_cmp

        elif h1_category == 'Pair':
            # find the pair and compare them.
            # if tied, compare kicker
            _, pair_h1 = is_pair(hand1)
            _, pair_h2 = is_pair(hand2)

            pair_cmp = pair_h1[0].compare(pair_h2[0])
            if pair_cmp == 0:
                # tied pair ranks
                for c1,c2 in zip(hand1, hand2):
                    cmp = c1.compare(c2)
                    if cmp != 0:
                        return cmp

                return 0 # all the same ranked cards
            return pair_cmp
        
        else:
            for i in range(len(hand1)):
                cmp = hand1[i].compare(hand2[i]) != 0:
                if cmp != 0:
                    return cmp
            return 0

def categorize_hand(hand):
    """
    Assign a category to a poker hand.
    param: hand (list of 5 cards)
    return: category of hand['Royal Flush', 'Straight Flush', etc.]
    rtype: str
    """
    global category_func_dict
    for category, func in category_func_dict.items():
        match, h = func(hand)
        if match:
            return category