import random

spices = ['N','O','P','Q','R','S','T']
correct_spice = ''
add = True

while add == True:
    spice = random.choice(spices)
    if spice not in correct_spice:
        correct_spice += spice
    if len(correct_spice) == 5:
        add = False

correct_spice = " ".join(correct_spice)
print(correct_spice)

game = True
attempts = []
inv = False

while game == True:
    exists = 0
    wrong_quantity = 0
    i = 0
    print("Previous attempts:")
    if len(attempts) == 0:
        print('No previous attempts')
    elif inv == False:
        attempts.reverse()
        for attempt in attempts:
            print(attempt)

    for_list = ''
    guess = input('Enter spice mix:\n')

    for letter in guess:
        if letter != ' ':
            if letter not in spices and inv == False:
                print('Invalid spice mix!')
                inv = True
                break
            else:
                inv = False
                if letter in correct_spice:
                    if guess[i] == correct_spice[i] and guess[i] != ' ':
                        exists += 1
                    if guess[i] != correct_spice[i] and guess[i] != ' ':
                        wrong_quantity += 1
        i += 1

    if inv == False:
        for_list = guess + ' (Good ' +str(exists)+', Wrong quantity '+str(wrong_quantity)+')'
        attempts.append(for_list)

    if guess == correct_spice:
        print("Congratulations!")
        game = False