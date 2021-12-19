from GenerateSpice import *
from Attempts import *

all_spices = GenerateSpice()
new_spice = all_spices.generate_spice()
lst = []
attempt = Attempts(lst)

class GuessMix:
    def __init__(self):
        self.for_list = ''
        self.guess()

    def guess(self):
        while attempt.game == True:
            i = 0
            exists = 0
            wrong_quantity = 0

            attempt.list_attempts()

            guess = input('Enter spice mix:\n')

            for letter in guess:
                if letter != ' ':
                    if letter not in all_spices.spices and attempt.inv == False:
                        print('Invalid spice mix!')
                        attempt.inv = True
                        break
                    else:
                        attempt.inv = False
                        if letter in new_spice:
                            if guess[i] == new_spice[i] and guess[i] != ' ':
                                exists += 1
                            if guess[i] != new_spice[i] and guess[i] != ' ':
                                wrong_quantity += 1
                i += 1

            if attempt.inv == False:
                self.for_list = guess + ' (Good ' + str(exists) + ', Wrong quantity ' + str(wrong_quantity) + ')'
                lst.append(self.for_list)

            if guess == new_spice:
                print("Congratulations!")
                attempt.game = False


game = GuessMix()
