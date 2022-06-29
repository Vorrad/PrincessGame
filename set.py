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
from common import GameError


class PlayerS(Player):
    """
    Player in a Set

    Attributes:
        hand_card: card player always keep
        round_card: card player only has at his/her round
        stat: player status, if is PLAYER_STAT[1] means cannot be chosen
    """

    def __init__(self, name=None):
        super(PlayerS, self).__init__(name)
        self.hand_card = Card(0)
        self.round_card = Card(0)
        self.stat = PLAYER_STAT[0]

    def set_stat(self, stat_no: 0 | 1):
        self.stat = PLAYER_STAT[stat_no]

    def draw_card(self, card: Card):
        if self.hand_card.id == 0:
            self.hand_card = card
        else:
            self.round_card = card

    def play_card(self, card_id: int) -> list:
        """unnecessary object filled with BLANK_VAL

        :param card_id: id of card to play
        :return: a list with 3 objects: card id + target player + val, empty when operation foul,
        """
        if card_id not in range(1, 9):
            print("Card id invalid, please choose a number from 1 to 8")
            return []

        if self.round_card.id == card_id:
            op = self.round_card.effect()
            return op

        elif self.hand_card.id == card_id:
            op = self.hand_card.effect()
            return op

        else:
            print("You don't have this card, please choose a card you have")
            return []

    def show_card_id(self):
        return self.hand_card.id, self.round_card.id

    def drop_card(self, card_id):
        if self.round_card.id == card_id:
            self.round_card = Card(0)
        elif self.hand_card.id == card_id:
            self.hand_card = self.round_card
            self.round_card = Card(0)
        else:
            raise GameError("in PlayerS.drop_card(): no such card!")


class Set(object):
    """Main part of game

    Attributes:
        active_player: player in current round, PlayerS class
        players: a list of PlayerS describes players alive
        deck: deck of cards on the table, defined in 'cards.py'
    """
    def __init__(self, suits=1):
        self.players = list()
        self.deck = Deck(suits)
        self.round_num = 0
        self.active_player = None

    def start(self, players: list, last_winner=None) -> str | None:
        """start the set

        :param players: list of PlayerS, reduce during the set
        :param last_winner: str, winner in last set
        :return: None | winner's name
        """
        if len(players) < 2:
            print("Participants less than 2!")
            return None
        self.players = players

        # Initial everyone's hand card and show all the players
        for player in self.players:
            print(player.name, end=' ')
            player.draw_card(self.deck.pop())
        print("Welcome to Princess Game!")
        self.show_players()

        if last_winner is None:  # First set in game
            self.active_player = self.players[random.randint(0, len(players) - 1)]
        else:
            self.active_player = self.find_player(last_winner)[1]
        assert type(self.active_player) == PlayerS
        print("The set start at:" + self.active_player.name)

        # Main loop
        while True:

            # Only one alive
            if len(self.players) <= 1:
                print("Game over, winner is " + self.players[0].name)
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
                    print("Game over, winner is " + top_player[0].name)
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

                # loop until player play it correctly
                target = list()
                while True:             # Check card id input
                    print("Please choose a card to play (enter 0 to discard a card): ", end="")
                    card_id = input().strip()
                    if not card_id.isdigit():
                        print("Invalid input, please type a number")
                        continue

                    # drop the card
                    if int(card_id) == 0:
                        print("Please choose a card:")
                        drop_id = input().strip()
                        if not drop_id.isdigit():
                            print("Not a number!")
                            continue
                        drop_id = int(drop_id)
                        if drop_id not in self.active_player.show_card_id():
                            print("You don't have this card!")
                            continue
                        target = (0, BLANK_VAL, drop_id)
                        break

                    target = self.active_player.play_card(int(card_id))
                    if not target:
                        continue
                    if target[1] == BLANK_VAL:
                        break

                    # Cannot choose self as target
                    if target[1] == self.active_player.name:
                        print("You cannot choose yourself as target!")
                        continue

                    # Check if target name exists
                    if not self.find_player(target[1]):
                        print("Invalid player name")
                        continue

                    break

                # Use the card and make it effect, or drop the card
                if target[0] == 0:
                    self.active_player.drop_card(target[2])
                else:
                    self.active_player.drop_card(target[0])
                    self.card_effect(target)

                # switch to next player
                index = self.players.index(self.active_player)
                if index == len(self.players) - 1:
                    index = 0
                else:
                    index += 1
                self.active_player = self.players[index]
                self.round_num += 1
                print("Round end, next player: " + self.active_player.name)

    def card_effect(self, op):
        """ method where cards' effects implement, will not check target_name's validity

        :param op: tuple of paras, card_id + target_name + target_val
        :return:
        """
        card_id, target_name, target_val = op
        assert card_id in range(1, 9)

        if card_id == 1:
            index, target = self.find_player(target_name)
            if target.hand_card.id == target_val:
                print("Oops, bingo! {} is out now!".format(target_name))
                self.players.pop(index)
                self.show_players()
            else:
                print("Sadly, you got it wrong")

        if card_id == 2:
            target = self.find_player(target_name)[1]
            print("Player {}'s hand is: {} {}".format(target_name, target.hand_card.id, target.hand_card.name))

        if card_id == 3:
            index, target = self.find_player(target_name)
            target_id = target.hand_card.id
            my_id = self.active_player.hand_card.id

            # win challenge
            if my_id > target_id:
                print("Your card has higher rank, {} is out!".format(target.name))
                self.players.pop(index)
                self.show_players()

            # lose challenge
            elif my_id < target_id:
                print("{} card has higher rank, you are out!".format(target.name))
                index = self.find_player(self.active_player.name)[0]

                # pop active_player, move active_player to former one before next round
                if index == 0:
                    self.active_player = self.players[-1]
                else:
                    self.active_player = self.players[index - 1]

                self.players.pop(index)
                self.show_players()

            # draw challenge
            else:
                print("Your card has the same rank with {}, nobody is out".format(target.name))

    def find_player(self, player_name) -> tuple | None:
        """ find a player in players by name, return a tuple

        :param player_name: str of player
        :return: index + player
        """
        for index, player in enumerate(self.players):
            if player.name == player_name:
                return index, player
        return None

    def show_players(self):
        print("Current players: ", end='')
        for player in self.players:
            print(player.name, end=' ')
        print()

    @staticmethod
    def target_protected(name):
        assert type(name) == str
        print("Your target {} is protected by handmaid please choose another target".format(name))

