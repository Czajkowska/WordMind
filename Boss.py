class Boss:
    def __init__(self, color):
        self.color = color
        self.hint = ""

        # Boss daje wskazowke swojej drozynie
    def action(self):
        self.hint = "hint"

        print(self.hint)
