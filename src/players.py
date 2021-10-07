"""
Author: Adrien Funel
Date: Sept-2021
Summary: create a player class with features
"""


class Player:
    """
    Class to generate the players of the tournament.
    """
    def __init__(self, id, power, technique, endurance):
        self.id = id
        self.power = power
        self.technique = technique
        self.endurance = endurance
        self.status = None

    def __str__(self):
        return "Id is {};\n " \
               "Power is {};\n " \
               "Technique is {};\n " \
               "Endurance is {}\n\n".format(self.id,
                                            self.power,
                                            self.technique,
                                            self.endurance
                                            )

    def playerid(self):
        """
        Function to return the identifier of the player.
        :return: int, the unique Id of the player
        """
        return self.id
