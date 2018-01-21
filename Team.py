class Team:

    def __init__(self, color):
        self.color = color
        self.guess = ""

        # Drozyna zgaduje pole
    def action(self):
        self.guess = "word"

        print(self.guess)
