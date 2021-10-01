"""
Author: Adrien Funel
Date: Sept-2021
Summary: simulate a competitive tennis game
"""
import random


def play_match(bracket):
    player1 = bracket['p1']
    player2 = bracket['p2']

    # score string example: 6-2;3-6;7-6;6-1

    # Play the tennis game here
    sets_p1 = 0
    sets_p2 = 0
    while sets_p1 < 3 and sets_p2 < 3:
        set_outcome = play_set(player1, player2)
        if set_outcome == "set p1":
            sets_p1 += 1
        elif set_outcome == "set p2":
            sets_p2 += 1

    if sets_p1 == 3:
        winner = player1
    elif sets_p2 == 3:
        winner = player2

    bracket.update({'seed': bracket['seed'],
                    'p1': bracket['p1'],
                    'p2': bracket['p2'],
                    'winner': winner,
                    'score': '6-2'})

    return bracket


def play_set(p1, p2):
    """
    Function to simulate a set.
    :param p1: player instance nb1
    :param p2: player instance nb2
    :return: string outcome of the set
    Needs a difference of 2 games.
    """
    games_p1 = 0
    games_p2 = 0
    id = 0
    while not (games_p1 >= 6 and abs(games_p1 - games_p2) >= 2) \
            and not (games_p2 >= 6 and abs(games_p1 - games_p2) >= 2) \
            and not (games_p1 == games_p2 == 6):
        game_outcome = play_game(p1, p2)
        if game_outcome == "game p1":
            games_p1 += 1
        elif game_outcome == "game p2":
            games_p2 += 1
        print(id)
        id += 1
        print("Set score is {}:{}".format(games_p1, games_p2))

    if games_p1 >= 6 and games_p2 < 6:
        return "set p1"
    elif games_p2 >= 6 and games_p1 < 6:
        return "set p2"
    elif games_p1 == games_p2 == 6:
        print("TIEBREAK")
        return play_tiebreak(p1, p2)


def play_game(p1, p2):
    """
    Function to simulate a game.
    :param p1: player instance nb1
    :param p2: player instance nb2
    :return: string outcome of the game

    0pt => love
    1pt => 15
    2pts => 30
    3pts => 40
    4pts => game
    In case of 40-40 => deuce
    """
    points_p1 = 0
    points_p2 = 0
    while not (points_p1 == 4 and abs(points_p1-points_p2) >= 2) \
            and not (points_p2 == 4 and abs(points_p1-points_p2) >= 2)\
            and not (points_p1 == 3 and points_p2 == 3):
        point_outcome = play_point(p1, p2)
        if point_outcome == "point p1":
            points_p1 += 1
        elif point_outcome == "point p2":
            points_p2 += 1
        elif point_outcome == "draw":
            pass
        print("{}:{}".format(points_p1, points_p2)
              .translate(str.maketrans({'1':'15',
                                        '2':'30',
                                        '3':'40',
                                        '4': 'game'}))+" score p1:p2")

    print("{}:{}".format(points_p1, points_p2)
          .translate(str.maketrans({'1': '15',
                                    '2': '30',
                                    '3': '40',
                                    '4': 'game'})) + " FINAL score p1:p2")

    if points_p1 == 4:
        return "game p1"
    elif points_p2 == 4:
        return "game p2"
    elif points_p1 == points_p2 == 3:
        return play_deuce(p1, p2)


def play_point(p1, p2):
    """
    Function to simulate a single point being played.
    :param p1: player instance nb1
    :param p2: player instance nb2
    :return: string outcome of the point
    """
    score1 = p1.power * p1.technique * p1.endurance * random.uniform(0, 1)
    score2 = p2.power * p2.technique * p2.endurance * random.uniform(0, 1)
    if score1 > score2:
        return "point p1"
    elif score1 < score2:
        return "point p2"
    else:
        return "draw"


def play_deuce(p1, p2):
    """
    Function to simulate a deuce played if the game is a draw at 40-40.
    :param p1: player instance nb1
    :param p2: player instance nb2
    :return: string outcome of the deuce point
    """
    deuce_points = 0
    while -2 < deuce_points < 2:
        deuce_outcome = play_point(p1, p2)
        if deuce_outcome == "point p1":
            deuce_points += 1
        elif deuce_outcome == "point p2":
            deuce_points -= 1

        print("Deuce points are {}".format(deuce_points)
              .translate(str.maketrans({'0': '40',
                                        '1': 'Ad',
                                        '2': 'game'})) + " score p1:p2")

    if deuce_points == 2:
        return "game p1"
    elif deuce_points == -2:
        return "game p2"


def play_tiebreak(p1, p2):
    """
    Function to simulate a tiebreak played if the set is a draw at 6-6.
    :param p1: player instance nb1
    :param p2: player instance nb2
    :return: string outcome of the tiebreak
    Tiebreak can be won in 7pts with a difference of 2.
    """
    tie_score = [0, 0]

    while not (tie_score[0] >= 7 and abs(tie_score[0] - tie_score[1]) >= 2) \
            and not (tie_score[1] >= 7 and abs(tie_score[0] - tie_score[1]) >= 2):
        tiebreak_outcome = play_point(p1, p2)
        if tiebreak_outcome == "point p1":
            tie_score[0] += 1
        elif tiebreak_outcome == "point p2":
            tie_score[1] += 1
        print("Tiebreak score is {}".format(tie_score))

    print("Tiebreak final score is {}:{}".format(tie_score[0], tie_score[1]))
    if tie_score[0] > tie_score[1]:
        return "set p1"
    elif tie_score[0] < tie_score[1]:
        return "set p2"
