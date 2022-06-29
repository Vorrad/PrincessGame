from set import PlayerS, Set


def main():
    _player_list = [PlayerS("Alice"), PlayerS("Bob"), PlayerS("Cate"), PlayerS("Dylan")]
    s = Set()
    s.start(_player_list)


if __name__ == '__main__':
    # 游戏开始！
    main()
