#!/usr/bin/env python3
"""P54 - Poker Hands"""

from sys import argv


class PokerHand(object):
    """Poker hands are ranked as follows:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit."""
    def __init__(self, hand):
        """Determines the value of the current hand."""
        self.ranked_hands = [
            self._straight_flush, self._four_of_a_kind, self._full_house,
            self._flush, self._straight, self._three_of_a_kind,
            self._two_pair, self._pair, self._high_card]
        self.cards = sorted((Card(c) for c in hand.split(' ')),
                            key=lambda x: x.value)
        self.num_cards = len(self.cards)
        self.specific_values = []

        for i, possible in enumerate(self.ranked_hands):
            if possible():
                self.hand_value = i
                break

    def __gt__(self, other):
        """Compare two poker hands. Returns a positive value if self wins,
        a negative value if other wins, and 0 if the hands are equal."""
        if self.hand_value != other.hand_value:
            return other.hand_value > self.hand_value
        else:
            for val, otherval in zip(self.specific_values, other.specific_values):
                if val != otherval:
                    return val > otherval
            for card, othercard in zip(self.cards[::-1], other.cards[::-1]):
                if card != othercard:
                    return card.value > othercard.value
        return False

    # The following methods check for specific types of hand.
    def _straight_flush(self):
        return self._flush() and self._straight()

    def _four_of_a_kind(self):
        return self._n_matching(4)

    def _full_house(self):
        if (self.cards[0] == self.cards[1] and
                (self.cards[1] == self.cards[2] or
                 self.cards[2] == self.cards[3]) and
                self.cards[3] == self.cards[4]):
            self.specific_values = [self.cards[0].value, self.cards[4].value]

    def _flush(self):
        suit = self.cards[0].suit
        for i in range(1, self.num_cards):
            if self.cards[i].suit != suit:
                return False
        return True

    def _straight(self):
        for i in range(1, self.num_cards):
            if self.cards[i].value - self.cards[i - 1].value != 1:
                return False
        self.specific_values.append(self.cards[-1].value)
        return True

    def _three_of_a_kind(self):
        return self._n_matching(3)

    def _two_pair(self):
        num_pairs = 0
        prev = self.cards[0].value
        self.specific_value = []
        for i in range(1, self.num_cards):
            if self.cards[i].value == prev:
                num_pairs += 1
                self.specific_values.append(prev)
                prev = None
            else:
                prev = self.cards[i].value
        if num_pairs == 2:
            return True
        return False

    def _pair(self):
        return self._n_matching(2)

    def _high_card(self):
        return True

    def _n_matching(self, n):
        """Returns True if there are at least n cards with matching values,
        False otherwise. The value of the matching cards is stored as a
        specific value."""
        prev = self.cards[0].value
        count = 1
        for i in range(1, self.num_cards):
            if self.cards[i].value == prev:
                count += 1
            else:
                prev = self.cards[i].value
                count = 1
            if count == n:
                self.specific_values.append(prev)
                return True
        return False


class Card(object):
    """A card has both a value and suit. Expect input of form e.g: '6H' = six
    of hearts."""
    values = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7,
              'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
    suits = {'H': 0, 'C': 1, 'S': 2, 'D': 3}

    def __init__(self, card):
        self.value = self.values[card[0]]
        self.suit = self.suits[card[1]]


if __name__ == '__main__':
    try:
        f = open(argv[1], 'r')
    except IndexError:
        print("Specify filename on command line")
    else:
        with f:
            all_hands = f.readlines()

        count = 0
        for hand in all_hands:
            if PokerHand(hand[0:14]) >  PokerHand(hand[15:]):
                count += 1

        print("Player 1 wins {0} hands".format(count))

