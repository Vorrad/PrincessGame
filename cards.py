"""
This module defines cards for Princess Game.
Including separate Card and Deck.
"""
from random import shuffle
from common import CARD_SUIT, BLANK_VAL
from common import GameError


class Card:
    """
    One card in game.

    Attributes:
        id: id of card, shows card's name and effect
        name: name of card, as a str
        effect: effect when card is played, print hints and check the input
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

    @staticmethod
    def guard_eff() -> tuple:

        print("You played a guard.\nPlease enter the player you want to guess:")
        player = input().strip()
        print("Please enter the card id you want to guess:")
        # loop until player play it correctly
        while True:
            val = input()
            if not val.isdigit():
                print("Invalid input, please type a number: ", end='')
                continue
            val = int(val)
            if val not in range(2, 9):
                print("Invalid card id, please choose a number from 2 to 8: ", end='')
                continue
            break
        return 1, player, val

    @staticmethod
    def priest_eff():
        print("I'm a priest")
        return [2, BLANK_VAL, BLANK_VAL]

    @staticmethod
    def baron_eff():
        print("I'm a baron")
        return [3, BLANK_VAL, BLANK_VAL]

    @staticmethod
    def handmaid_eff():
        print("I'm a handmaid")
        return [4, BLANK_VAL, BLANK_VAL]

    @staticmethod
    def prince_eff():
        print("I'm a prince")
        return [5, BLANK_VAL, BLANK_VAL]

    @staticmethod
    def king_eff():
        print("I'm a king")
        return [6, BLANK_VAL, BLANK_VAL]

    @staticmethod
    def countess_eff():
        print("I'm a countess")
        return [7, BLANK_VAL, BLANK_VAL]

    @staticmethod
    def princess_eff():
        print("I'm a princess")
        return [8, BLANK_VAL, BLANK_VAL]


class Deck:
    """ Deck for a set

    Attributes:
        cards: list of cards in the deck
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

    def count(self) -> int:
        return len(self.cards)
