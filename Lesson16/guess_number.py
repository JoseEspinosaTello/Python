# guess my number

#We are passing a command line argument to the game so that we can personalize the game. rps8

import sys
import random


def guess_number(name='PlayerOne'):
    game_count = 0
    player_wins = 0
  

    #make game a function

    def play_guess_number():

        nonlocal name # param from rps function
        nonlocal player_wins
       
        playerchoice = input(f"\n{name}, guess which number I'm thinking of... 1, 2, or 3.\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_guess_number( ) #recursion to start function again

        # need to cast the value from string to int for use in if statement
        player = int(playerchoice)

        # computer will use random to make a choice between the 3 values given,
        computerchoice = random.choice("123")

        #cast to int
        computer = int(computerchoice)

        # space in command line
        

        print(f"\n{name}, you  chose {player}.") #pass the player value into rps class to pull either rock, paper, scissors. 
        #used .replace to remove RPS from the line
        # title returns value with capital first letter
        print(f"I was thinking about the number {computer}.")
        
        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
           

            if player == computer:
                player_wins +=1
                return f"🎉 {name}, you win"
            elif player != computer:
                
                return f"Sorry {name}, better luck next time. 🤣😒🤣"
            
            
        game_result = decide_winner(player, computer) #call function and assign to new variable

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name} wins: {player_wins}")
        print(f"\nYour win percentage {player_wins / game_count:.2%}")

        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\n Y for Yes or \n Q to Quit \n\n")

            if playagain.lower() not in ["y", "q"]: #if answer is not y or q will ask the question again
                continue
            else:
                break # if answer is y or q will break while loop and move to next if statment

        if playagain.lower() == "y": # if answer is y will use recursive function to start game again
            return play_guess_number() #recursive function
        else: # if answer anything other than y will end the game
            print("\n🥳🥳🥳🥳") # window key + . for emojis
            print("Thank you for playing\n")

            #If the file is run alone, then by default __name__ = "__main__"
            if __name__ == "__main__": #if this is the case then name = main and we will close the game by using sys.exit
                sys.exit(f"Bye {name}! 👋")
            else:
                return # if it was launched from the arcade file we want an empty return and that will take it back to the parent function which will be in arcade file

    return  play_guess_number #recursion to start function again

# if __name__ == "__main__":
#     guess_number()

if __name__ == "__main__":
    import argparse #command ling option and argument parsing library

    parser =argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )


    args= parser.parse_args()
    guess_number_game = guess_number(args.name)
    guess_number_game() #lesson on closures
