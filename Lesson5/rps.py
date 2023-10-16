import sys
import random

#intruction to python enum
from enum import Enum

class RPS(Enum):
   
   #USE all caps for contstant variables
   ROCK = 1
   PAPER = 2
   SCISSORS = 3

print(RPS(2))
print(RPS.ROCK)
print(RPS['ROCK'])
print(RPS.ROCK.value)
#sys.exit() # will stop rest of code from running

# # Accept user input 

# value = input('Please enter a value:\n')

# print(value)

# Create Rock Paper Scissors game.

print("")
playerchoice = input("Enter... \n1 for Rock,\n2 for paper, or \n3 for Scissors:\n\n")

# need to cast the value from string to int for use in if statement
player = int(playerchoice)

#start applying control flow to our program
# procedural control flow

# if 1 > 2:
#     print('do somthing')

if player > 1 | player > 3:
   sys.exit(print("You must enter 1, 2, or 3."))

# computer will use random to make a choice between the 3 values given,
computerchoice = random.choice("123")

#cast to int
computer = int(computerchoice)

# space in command line
print("")

print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
#used .replace to remove RPS from the line
print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
print("")
22
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
   