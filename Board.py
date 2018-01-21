import random
from Field import *
from Color import *


class Board:
    def __init__(self, size=(5, 5), how_many_colors=2):
        self.size = size
        self.how_many_colors = how_many_colors - 1

        self.actualColor = Color(random.randint(0, self.how_many_colors))

        self.actualBoard = []

        for row in range(self.size[0]):
            self.actualBoard.append([])

        self.key = []

        for row in range(self.size[0]):
            self.key.append([])

        # Wylosuj odpowiednia ilosc slow z bazy
    def get_words(self):
        file = open("words.txt", "r")

        all_words = file.readlines()

        file.close()

        how_many_words = self.size[0] * self.size[1]

        choosen_words = []

        while how_many_words > 0:
            while True:
                position = random.randint(0, len(all_words) - 1)
                if not all_words[position] in choosen_words:
                    break

            choosen_words.append(all_words[position])
            how_many_words -= 1

        return choosen_words

        # Wgeneruj plansze
    def create_board(self):
        words = self.get_words()

        position = 0

        for row in range(self.size[0]):
            for column in range(self.size[1]):
                self.actualBoard[row].append(Field(words[position]))

                self.key[row].append(Field(words[position]))

                position += 1
        self.show_board()

    def painting(self, new_color, how_many_words, what_to_paint):
        while how_many_words > 0:
            while True:
                row = random.randint(0, self.size[0] - 1)
                column = random.randint(0, self.size[1] - 1)

                if what_to_paint == "key":
                    if self.key[row][column].color == Color.EMPTY:
                        break

            if what_to_paint == "key":
                self.key[row][column].changeColor(new_color)

            how_many_words -= 1

        # Stworz klucz bedacy plansza z wyznaczonymi kolorami pol
    def create_key(self, how_many_color_words=8, how_many_black=1):
        how_many_colors = self.how_many_colors

        while how_many_colors >= 0:
            if self.actualColor == Color(how_many_colors):
                self.painting(Color(how_many_colors), how_many_color_words + 1, "key")
            else:
                self.painting(Color(how_many_colors), how_many_color_words, "key")

            how_many_colors -= 1

        self.painting(Color.BLACK, how_many_black, "key")

        for row in range(len(self.key)):
            for column in range(len(self.key[row])):
                if self.key[row][column].color == Color.EMPTY:
                    self.key[row][column].change_color(Color.NEUTRAL)

        # Tmp metoda do ladnego wyswietlania planszy i klucza
    def pretty_print(self, what_to_print):
        tmp = []

        for i in what_to_print:
            for j in i:
                tmp.append(j.to_str())

        c = 0
        for i in range(self.size[0]):
            print(tmp[c: c + self.size[1]])
            c += self.size[1]

        # Wswietlanie planszy
    def show_board(self):
        print("Board:")

        self.pretty_print(self.actualBoard)

        print()

        # Wyswietlanie klucza
    def show_key(self):
        print("Key:")

        self.pretty_print(self.key)

        print()

        # Odkrywa pole na planszy
    def update_board(self, position):
        self.actualBoard[position[0]][position[1]] = self.key[position[0]][position[1]]

        # Zmienia graczy na nastepny kolor
    def switch_color(self):
        if self.actualColor == Color(self.how_many_colors):
            self.actualColor = Color.RED
        else:
            self.actualColor = Color(self.actualColor.value + 1)