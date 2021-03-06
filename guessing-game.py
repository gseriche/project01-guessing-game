"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally
do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

def guess(number):
    the_number = random.randint(1,10)
    counter = 0
    while(the_number != number):
        try:
            number = int(input("Guess again!: "))
            counter += 1
            if (number >= 1) and (number <= 10):
                if number > the_number:
                    print("It's lower.")
                elif number < the_number:
                    print("It's higher.")
            else:
                print("You must enter numbers between 1 to 10")
        except:
            print("You must enter only numbers, told you before!")

    print("Got it!")
    return counter


def start_game():
    print('''

    --- Welcome to the great guessing game ---

    ''')

    ask = "yes"
    count = 0

    while (ask == "yes") or (ask == "y"):
        if count > 0:
            print("The last highscore was {} attempts".format(count))

        try:
            number = int(input("Guess the number: "))
        except:
            print("You must input only numbers")
        else:
            if ((number >= 1) and (number <= 10)):
                count = guess(number)
                print("You made it in {} attempts!".format(count))
            else:
                print("You must enter a number between 1 to 10")
            try:
                ask = str(input("Do you wanna play again? [yes/no]:"))
            except:
                print("You must enter yes, y or no")

    print('''

    --- Thank you for play with us this great game ---

    ''')

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
