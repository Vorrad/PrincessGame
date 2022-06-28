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
from common import PLAYER_STAT, BLANK_VAL


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

    def play_card(self, card_id: int) -> list:
        """
        unnecessary object filled with BLANK_VAL

        :param card_id: id of card to play
        :return: a list with 3 objects: card id + target player + val, empty when operation foul,
        """
        if card_id not in range(1, 9):
            print("Card id invalid, please choose a number from 1 to 8")
            return []

        if self.round_card.id == card_id:
            op = self.round_card.effect()
            self.round_card = Card(0)
            return op

        elif self.hand_card.id == card_id:
            op = self.hand_card.effect()
            self.hand_card = self.round_card
            self.round_card = Card(0)
            return op

        else:
            print("You don't have this card, please choose a card you have")
            return []


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

        # Initial everyone's hand card and show all the players
        print("Welcome to Princess Game!\nPlayers in the set:", end='')
        for player in self.players:
            print(player.name, end=' ')
            player.draw_card(self.deck.pop())
        print()

        if last_winner is None:  # First set in game
            self.active_player = self.players[random.randint(0, len(players) - 1)]
        else:
            self.active_player = last_winner
        assert type(self.active_player) == PlayerS
        print("The set start at:", self.active_player.name)


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

                # loop until player play it correctly
                while True:             # Check card id input
                    card_id = input()
                    if not card_id.isdigit():
                        print("Invalid input, please type a number")
                        continue
                    break

                while True:             # Check target
                    target = self.active_player.play_card(int(card_id))
                    if not target:
                        continue
                    if target[1] == BLANK_VAL:
                        break
                    target_name = target[1]

                    # check if target name exists
                    if not self.find_player(target_name):
                        print("Invalid player name")
                        continue

                self.card_effect(target)

                # switch to next player
                index = self.players.index(self.active_player)
                if index == len(self.players) - 1:
                    index = 0
                else:
                    index += 1
                self.active_player = self.players[index]
                self.round_num += 1
                print("Round end, next player: ", self.active_player.name)

    def card_effect(self, op):
        """
        method where cards' effects implement

        :param op:
        :return:
        """
        card_id, target_name, target_val = op
        assert card_id in range(1, 9)

        if card_id == 1:
            index, target = self.find_player(target_name)
            if target.hand_card.id == target_val:
                print("Oops, bingo!")
                self.players.pop(index)
            else:
                print("Sadly, you got it wrong")

    def find_player(self, player_name) -> list | None:
        """

        :param player_name:
        :return: list of 2: index + player
        """
        for index, player in enumerate(self.players):
            if player.name == player_name:
                return [index, player]
        return None

