import random


class Dice:
    def __init__(self, sides):
        self.__sides = sides
        self.__name = "{} sided dice".format(sides)

    def roll(self):
        print(random.randint(1,self.__sides))

    def myName(self):
        return self.__name


def addDice(allDice):
    sides = input("How many sides should the dice have?\n")
    if sides.isdigit() == False:
        print("Only numbers accepted!")
        return 0
    sides = float(sides)
    sides = abs(round(sides))
    if sides < 0:
        print("Cant have 0 sides!")
        return 0

    new = Dice(sides)
    allDice[new.myName()] = new


def removeDice(allDice):
    listDice(allDice)
    sas = {}
    choice = input("Remove the desired dice by typing in its number\n")
    if "{} sided dice".format(choice) not in allDice:
        return 0
    sas.remove("{} sided dice".format(choice))


def listDice(allDice):
    for i in allDice:
        print(i)


def main():
    allDice = {}
    print('Welcome to gambling. Press A to add a dice, D to delete a dice, L to list all available dice')
    print('\nPress "R" to roll a specific dice, and RA to roll all the dice.\nQ to quit, HELP to get help. Ty 4 moneys')
    cmd = ''
    while cmd != 'q':
        cmd = input("> ")
        if cmd.isalpha() or cmd == '':
            cmd = cmd.lower()
        else:
            print("Banned 4 life")
            return 0


        if cmd == 'help':
            main()
            return 0
        if cmd == 'a':
            addDice(allDice)
        if cmd == 'd':
            removeDice(allDice)
        if cmd == 'r':
            throw = input("Which dice do you wish to throw? (Answer with the number of sides, or all to.. well throw all of them.)\n")
            if throw == 'all':
                for i in allDice:
                    print(allDice[i].myName() + ":")
                    allDice[i].roll()
                    print()
            elif '{} sided dice'.format(throw) in allDice:
                allDice['{} sided dice'.format(throw)].roll()

        if cmd == 'l':
            print('Available dice:')
            listDice(allDice)
            print('     -----     ')

        
main()
