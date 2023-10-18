#use loops to improve rock, paper scissors    

import sys
import random

#intruction to python enum
from enum import Enum

class RPS(Enum):
   
   #USE all caps for contstant variables
   ROCK = 1
   PAPER = 2
   SCISSORS = 3

playagain = True

while playagain:

    print(RPS(2))
    print(RPS.ROCK)
    print(RPS['ROCK'])
    print(RPS.ROCK.value)
    #sys.exit() # will stop rest of code from running

    # # Accept user input 

    # value = input('Please enter a value:\n')

    # print(value)

    # Create Rock Paper Scissors game.

    
    playerchoice = input("\nEnter... \n1 for Rock,\n2 for paper, or \n3 for Scissors:\n\n")

    # need to cast the value from string to int for use in if statement
    player = int(playerchoice)

    #start applying control flow to our program
    # procedural control flow

    # if 1 > 2:
    #     print('do somthing')

    if player <1 or player > 3:
        sys.exit(print("You must enter 1, 2, or 3."))

    # computer will use random to make a choice between the 3 values given,
    computerchoice = random.choice("123")

    #cast to int
    computer = int(computerchoice)

    # space in command line
    

    print("\nYou chose " + str(RPS(player)).replace('RPS.', '') + ".")
    #used .replace to remove RPS from the line
    print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".\n")
   
    if player == 1 and computer == 3:
        print("🎉 You win")
    elif player == 2 and computer == 1:
        print("🎉 You win")
    elif player == 3 and computer == 1:
        print("🎉 You win")
    elif player == computer:
        print("😲 Tie Game!")
    else:
        print("🐍🐍🐍 Python wins!")

    playagain = input("\nPlay again?\n Y for Yes or \n Q to Quit \n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\n🥳🥳🥳🥳") # window key + . for emojis
        print("Thank you for playing\n")
        playagain = False

sys.exit("Bye 👋")