"""
This module defines class 'Set'
which represents one set in a hole multiplayer game.

It contains following properties
    1. deck on the table
    2. alive player list
    3. current round
"""
import random
from typing import Any

from cards import Deck, Card
from player_list import Player
from common import PLAYER_STAT


class PlayerS(Player):
    """
    Player in a Set
    """

    def __init__(self):
        super(PlayerS, self).__init__()
        self.hand_card = Card(0)  # The card player always keep
        self.round_card = Card(0)  # The card player only has at his/her round
        self.stat = PLAYER_STAT[0]

    def set_stat(self, stat_no: 0 | 1):
        self.stat = PLAYER_STAT[stat_no]

    def draw_card(self, card: Card):
        if self.hand_card.id == 0:
            self.hand_card = card
        else:
            self.round_card = card

    def play_card(self, card_id: int) -> bool:
        """
        Return False when operation foul
        """
        if card_id not in range(1, 9):
            print("Card id invalid, please choose a number from 1 to 8")
            return False

        if self.round_card.id == card_id:
            self.round_card.effect()
            self.round_card = Card(0)
            return True

        elif self.hand_card.id == card_id:
            self.hand_card.effect()
            self.hand_card = self.round_card
            self.round_card = Card(0)
            return True

        else:
            print("You don't have this card, please choose a card you have")
            return False


class Set:
    def __init__(self, suits=1):
        self.players = list()
        self.deck = Deck(suits)
        # TODO: Implement class Round, replace this with a round object
        self.round_num = 0
        self.active_player = None

    def start(self, players: list, last_winner=None) -> str | None:
        """
        start the set

        :param players: list of PlayerS, reduce during the set
        :param last_winner: PlayerS, winner in last set
        :return: None | winner's name
        """
        if len(players) < 2:
            print("Participants less than 2!")
            return None
        self.players = players

        if last_winner is None:  # First set in game
            self.active_player = self.players[random.randint(0, len(players) - 1)]
        else:
            self.active_player = last_winner
        assert type(self.active_player) == PlayerS
        print("The set start at: ", self.active_player.name)

        # Initial everyone's hand card
        for player in self.players:
            player.draw_card(self.deck.pop())

        # Main loop
        while True:

            # Only one alive
            if len(self.players) <= 1:
                print("Game over, winner is ", self.players[0].name)
                return self.players[0].name

            # No more card in the deck
            elif self.deck.count() == 0:
                top_card = 0
                top_player = []

                for player in self.players:
                    assert type(player) == PlayerS
                    if player.hand_card.id > top_card:
                        top_card = player.hand_card.id
                        top_player = [player]
                    elif player.hand_card.id == top_card:
                        top_player.append(player)

                if len(top_player) > 1:
                    print("Draw game, no winner")
                    return None
                else:
                    print("Game over, winner is ", top_player[0].name)
                    return top_player[0].name

            # Game continue
            else:
                # Reset stat
                self.active_player.set_stat(0)

                # Draw a card
                self.active_player.draw_card(self.deck.pop())

                # Play a card
                print("Your current cards are:")
                print(self.active_player.hand_card.id, self.active_player.hand_card.name)
                print(self.active_player.round_card.id, self.active_player.round_card.name)
                print("Please choose a card to play: ", end="")
                # TODO: here is a bug when input is invalid, it will jump over the player
                try:
                    # loop until player play it correctly
                    while not self.active_player.play_card(int(input())):
                        continue
                except ValueError:
                    print("Invalid input!")

                # search current player in the player list
                index = self.players.index(self.active_player)
                if index == len(self.players) - 1:
                    index = 0
                else:
                    index += 1
                self.active_player = self.players[index]
                print("Round end, next player: ", self.active_player.name)

    def play_round(self):
        pass
