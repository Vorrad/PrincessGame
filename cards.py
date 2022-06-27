"""
This module defines cards for Princess Game.
Including separate Card and Deck.
"""


class Card:
    """
    One card in game. Properties:
    1. id
    2. name
    3. effect
    """
    def __init__(self, card_id: int):
        self.id = card_id

        if self.id == 1:
            self.name = "Guard"
            self.effect = self.guard_eff
        if id == 2:
            self.name = "Priest"
            self.effect = self.priest_eff
        if self.id == 3:
            self.name = "Baron"
            self.effect = self.baron_eff
        if self.id == 4:
            self.name = "Handmaid"
            self.effect = self.handmaid_eff
        if self.id == 5:
            self.name = "Prince"
            self.effect = self.prince_eff
        if self.id == 6:
            self.name = "King"
            self.effect = self.king_eff
        if self.id == 7:
            self.name = "Countess"
            self.effect = self.countess_eff
        if self.id == 8:
            self.name = "Princess"
            self.effect = self.princess_eff

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
