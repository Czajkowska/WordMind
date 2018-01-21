from Color import *


class Field:
    def __init__(self, word, color=Color.EMPTY):
        self.word = word
        self.color = color

        # Ustawia nowy kolor pola na zadany
    def change_color(self, new_color):
        self.color = new_color

        # Tmp netoda do wyswietlania pol
    def to_str(self):
        return [self.word, self.color.name]
