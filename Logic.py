from Board import *
from Group import *
from Color import *


class Logic:
    def __init__(self):
        self.who = Color.RED
        self.board = Board()

        self.playersList = []

        for color in range(self.board.how_many_colors+1):
            self.playersList.append(Group(Color(color)))

        # Wswietlanie menu
    def menu(self):
        print("--MENU--")
        print("New game")
        print("Exit")

        # Tworzy plansze i klucz
    def create_board_and_key(self):
        self.board.create_board()
        self.board.create_key()

        # Pokazuje szefowi klucz i pozwala mu podac wskazowke
    def boss_action(self, color):
        self.board.show_key()
        self.playersList[color.value].boss.action()

        # Pokazuje drozynie plansze i pozwala im wybrac pole
    def team_action(self, color):
        self.board.show_board()
        self.playersList[color.value].team.action()

        # Zmienia grupe na inny kolor
    def switch_color(self):
        self.board.switch_color()

        # Wyswietla kto wygral
    def winner(self):
        print("! ! ! Color ", self.board.actualColor.name, " wins ! ! !")

        # Przed wyjsciem z gry
    def end_state(self):
        print("Thank you, bye!")
