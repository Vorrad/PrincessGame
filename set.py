"""
This module defines class 'Set'
which represents one set in a hole multiplayer game.

It contains following properties
    1. deck on the table
    2. alive player list
    3. current round
"""
from cards import Deck, Card
from player_list import Player, PlayerList


class PlayerS(Player):
    """
    Player in a Set
    """
    def __init__(self):
        super(PlayerS, self).__init__()
        self.hand_card = Card()   # The card player always has
        self.round_card = Card()  # The card player only has at his/her round


class Set:
    def __init__(self, suits=1):
        self.players = list()
        self.deck = Deck(suits)
        # TODO: Implement class Round, replace this with a round object
        self.round_num = 1

    def start(self, players: PlayerList):
        if players.count() < 2:
            print("Participants less than 2!")
            return
        self.players = players

