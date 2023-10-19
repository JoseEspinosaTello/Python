#use loops to improve rock, paper scissors    

import sys
import random

#intruction to python enum
from enum import Enum

#make game a function

def play_rps():
    class RPS(Enum):
   
        #USE all caps for contstant variables
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    

    playerchoice = input("\nEnter... \n1 for Rock,\n2 for paper, or \n3 for Scissors:\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps( ) #recursion to start function again

    # need to cast the value from string to int for use in if statement
    player = int(playerchoice)

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

    print("\nPlay again?")

    while True:
        playagain = input("\n Y for Yes or \n Q to Quit \n\n")

        if playagain.lower() not in ["y", "q"]: #if answer is not y or q will ask the question again
            continue
        else:
            break # if answer is y or q will break while loop and move to next if statment

    if playagain.lower() == "y": # if answer is y will use recursive function to start game again
         return play_rps() #recursive function
    else: # if answer anything other than y will end the game
        print("\n🥳🥳🥳🥳") # window key + . for emojis
        print("Thank you for playing\n")
        sys.exit("Bye 👋")

play_rps()