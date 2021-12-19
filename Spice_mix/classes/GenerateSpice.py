import random


class GenerateSpice:
    def __init__(self):
        self.spices = ['N', 'O', 'P', 'Q', 'R', 'S', 'T']
        self.correct_spice = ''
        self.add = True

    def generate_spice(self):
        while self.add == True:
            spice = random.choice(self.spices)
            if spice not in self.correct_spice:
                self.correct_spice += spice
            if len(self.correct_spice) == 5:
                self.add = False

        self.correct_spice = " ".join(self.correct_spice)

        return self.correct_spice