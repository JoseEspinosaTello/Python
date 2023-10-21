#we are making rps7 a module

import sys
import random

#intruction to python enum
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    #make game a function

    def play_rps():

        nonlocal player_wins
        nonlocal python_wins

        
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
        

        print(f"\nYou chose {str(RPS(player)).replace('RPS.', '').title()}.")
        #used .replace to remove RPS from the line
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")
        
        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins +=1
                return "🎉 You win"
            elif player == 2 and computer == 1:
                player_wins +=1
                return "🎉 You win"
            elif player == 3 and computer == 1:
                player_wins +=1
                return "🎉 You win"
            elif player == computer:
                return "😲 Tie Game!"
            else:
                python_wins += 1
                return "🐍🐍🐍 Python wins!"
            
        game_result = decide_winner(player, computer) #call function and assign to new variable

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {str(game_count)}")
        print(f"\nPlayer wins: {str(player_wins)}")
        print(f"\nPython wins: {str(python_wins)}")

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

    return play_rps

rock_paper_scissors = rps()

if __name__ == "__main__":
    rock_paper_scissors()
