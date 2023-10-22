import sys
from rps import rps
from guess_number import guess_number


def play_arcade(name = "PlayerOne"):

    welcome_back = False # boolean when game returns from other game module

    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu.")

        playerchoice = input(f"Please choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press \"x\" to exit the Arcade.\n")

        if playerchoice not in ["1", "2", "x"]:
            print(f"{name}, please enter 1, 2, or x.\n")
                
            return play_arcade(name) # recursion: need to return the function to start over
        
        welcome_back = True 
        
        if playerchoice == "1":
            rock_paper_scissors= rps(name) # name value was passed as a param in play_arcade func
            #we use closure to pass it to rps function
            rock_paper_scissors() #call function 
        elif playerchoice == "2":
            guess_my_numnber = guess_number(name)
            guess_my_numnber()
        elif playerchoice == "x":
            print("\n🥳🥳See you next time!🥳🥳") # window key + . for emojis
            print("Thanks for playing\n")
            sys.exit(f"Bye {name}! 👋")
        else:
            print(" ")
            print(f"\n\n\n{name}, please enter 1, 2, or x.\n")




if __name__ == "__main__":
    import argparse #command ling option and argument parsing library

    parser =argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the Arcade! 🤖🤖\n")

    
    play_arcade(args.name)
    
