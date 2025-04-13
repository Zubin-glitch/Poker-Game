from card import Card
from deck import Deck
from poker_hands import *
from poker_rules import *
from poker_stats import *

table = []
deck = Deck()
deck.shuffle()

table = [deck.deal_card() for _ in range(5)]
test_hand = [deck.deal_card() for _ in range(2)]

total_hand = table + test_hand

# print(f"Table: {table}")
# print(f"Hand: {test_hand}")
print(f'Table plus cards in hand: {total_hand}')
total_hand.sort(reverse=True)
print(f'Sorted hand: {total_hand}')

best_rank = ['High Card']

def calculate_highest_combo(hand, idx, slate, best_rank):
    # Backtracking case: intermediate worker
    if len(slate) == 5:
        # compute the hand rank
        curr_rank = compute_hand(slate)
        # if curr_rank < best_rank:
        #     best_rank = curr_rank
        #     return
        # Update best_rank if a better hand is found:
        if hand_categories.index(curr_rank) > hand_categories.index(best_rank[0]):
            print(f'Change of best hand from {best_rank[0]} to {curr_rank}')
            best_rank[0] = curr_rank
            return
    
    # Base case: Leaf worker
    if idx == len(hand):
        return
    
    # Recursive case: Internal node worker
    # I have two choices:

    # exclude    
    calculate_highest_combo(hand, idx + 1, slate, best_rank)

    # include
    slate.append(hand[idx])
    calculate_highest_combo(hand, idx + 1, slate, best_rank)
    slate.pop()

def compute_hand(hand: list[Card]) -> str:
    print(f"testing hand: {hand}")
    if is_royal_flush(hand)[0]:
        return 'Royal Flush'
    elif is_straight_flush(hand)[0]:
        return 'Straight Flush'
    elif is_four_of_a_kind(hand)[0]:
        return 'Four of a Kind'
    elif is_full_house(hand)[0]:
        return 'Full House'
    elif is_flush(hand)[0]:
        return 'Flush'
    elif is_straight(hand)[0]:
        print(f"Hand: {hand}")
        return 'Straight'
    elif is_three_of_a_kind(hand)[0]:
        return 'Three of a Kind'
    elif is_two_pair(hand)[0]:
        return 'Two Pair'
    elif is_pair(hand)[0]:
        return 'Pair'
    else:
        return 'High Card'

# test_hand = total_hand
test_hand = total_hand
# test_hand.append(Card('K', 'heart'))
# test_hand.append(Card('J', 'club'))
# test_hand.append(Card('10', 'spade'))
# test_hand.append(Card('7', 'diamond'))
# test_hand.append(Card('6', 'club'))
# test_hand.append(Card('3', 'heart'))
# test_hand.append(Card('3', 'spade'))
calculate_highest_combo(test_hand, 0, [], best_rank)
print(f"Calculated best rank:{best_rank}")

