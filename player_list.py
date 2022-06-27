"""
This module defines data struct PlayerList.
Other module can invoke them as base class.
"""
import random

from common import DEFAULT_NAME_LIST
from common import GameError


class Player:
    """
    properties:
        1. name (unique)
    """
    def __init__(self, name=None):
        # May occur repetition
        if name is None:
            # fill num to 5 digits
            self.name = DEFAULT_NAME_LIST[random.randint(0, len(DEFAULT_NAME_LIST)-1)] \
                        + str(random.randint(0, 99999)).zfill(5)
        else:
            self.name = name

    def rename(self, name):
        self.name = name


# class PlayerList:
#     """
#     properties:
#         1. name list
#         2. player list
#         3. player counts
#     """
#     def __init__(self):
#         self.names = []
#         self.players = {}
#         self.p_count = len(self.names)
#
#     def append(self, player: Player):
#         try:
#             if player.name in self.names:
#                 raise GameError("This name has been used, please change your name")
#             self.names.append(player.name)
#             self.players[player.name] = player
#             self.p_count += 1
#         except GameError as e:
#             print(e.arg)
#
#     def delete(self, player_name: str):
#         try:
#             if player_name not in self.names:
#                 raise GameError("This name does not exist")
#             self.names.remove(player_name)
#             self.players.pop(player_name)
#             self.p_count -= 1
#         except GameError as e:
#             print(e.arg)
#
#     def count(self) -> int:
#         return len(self.players)
#
#     def get_i(self, i) -> Player:
#         return self.players[i]


