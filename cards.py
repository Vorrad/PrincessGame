"""
This module defines cards for Princess Game.
Including separate Card and Deck.
"""
from random import shuffle
from common import CARD_SUIT
from common import GameError


class Card:
    """
    One card in game. Properties:
    1. id
    2. name
    3. effect
    """

    def __init__(self, card_id=0):
        self.id = card_id

        if self.id == 0:
            self.name = "Empty"
            self.effect = None
        elif self.id == 1:
            self.name = "Guard"
            self.effect = self.guard_eff
        elif self.id == 2:
            self.name = "Priest"
            self.effect = self.priest_eff
        elif self.id == 3:
            self.name = "Baron"
            self.effect = self.baron_eff
        elif self.id == 4:
            self.name = "Handmaid"
            self.effect = self.handmaid_eff
        elif self.id == 5:
            self.name = "Prince"
            self.effect = self.prince_eff
        elif self.id == 6:
            self.name = "King"
            self.effect = self.king_eff
        elif self.id == 7:
            self.name = "Countess"
            self.effect = self.countess_eff
        elif self.id == 8:
            self.name = "Princess"
            self.effect = self.princess_eff
        else:
            raise GameError("No such card id: " + str(card_id))

    # TODO: Replace effects with real functions
    @staticmethod
    def guard_eff():
        print("I'm a guard:")

    @staticmethod
    def priest_eff():
        print("I'm a priest")

    @staticmethod
    def baron_eff():
        print("I'm a baron")

    @staticmethod
    def handmaid_eff():
        print("I'm a handmaid")

    @staticmethod
    def prince_eff():
        print("I'm a prince")

    @staticmethod
    def king_eff():
        print("I'm a king")

    @staticmethod
    def countess_eff():
        print("I'm a countess")

    @staticmethod
    def princess_eff():
        print("I'm a princess")


class Deck:
    """
    Deck for a set
    """

    def __init__(self, suite_n=1):
        """
        Generate a deck

        :param suite_n: number of suits included in the deck
        """
        self.cards = list()

        cards_index = list()
        for i in range(0, suite_n):
            cards_index.extend(CARD_SUIT)
        shuffle(cards_index)

        for i in cards_index:
            self.cards.append(Card(i))

    def dump(self):
        print("Current deck (top to bottom):")
        for card in reversed(self.cards):
            print(card.id, ' ', end='')
        print()

    def pop(self) -> Card:
        return self.cards.pop()

    def count(self):
        return len(self.cards)
