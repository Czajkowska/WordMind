from Boss import *
from Team import *


class Group:
    def __init__(self, color):
        self.boss = Boss(color)
        self.team = Team(color)
        self.color = color
