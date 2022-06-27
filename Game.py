"""
This directory defines class 'Game'
which represents a hole multiplayer game.

It contains following properties
    1. number of rounds to win
    2. list of players
    3. number of players
    4. sequence of players
"""

_rounds_to_win = 4
_player_list = []
_player_seq = {}


class Game:
    def __init__(self,
                 rounds_to_win=_rounds_to_win,
                 player_list=None,
                 player_seq=None):

        if player_seq is None:
            player_seq = _player_seq
        if player_list is None:
            player_list = _player_list

        self.rounds_to_win = rounds_to_win
        self.player_list = player_list
        self.player_num = len(player_list)
        self.player_seq = player_seq

    def set_rtw(self, round_to_win):
        """
        Reset rounds to win for one game

        :param round_to_win: A signed number
        """

        self.rounds_to_win = round_to_win

    def set_pl(self, player_list):
        """
        Reset player list for one game

        :param player_list: List, consists players
        :return:
        """

        self.player_list = player_list
        self.player_num = len(player_list)

    def set_ps(self, player_seq):
        """
        Reset player sequence for one game

        :param player_seq: Dict, key in range(1, plyer_num + 1), value as player's ID
        :return:
        """

        self.player_seq = player_seq
