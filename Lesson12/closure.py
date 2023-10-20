# closure is a function having access to the scope of its parent function after the parent function has returned.

#will have a nested function definced, the nested function will have acces to its parent functions scope.

# creating a nested function and using closure is a good way to avoid polution your scope and creating to many global variables

def parent_function(person):
    coins = 3

    #parent function returns the play_game() function
    # then the play_game() function has access to the scope of the parent function.

    def play_game():
        nonlocal coins 
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")

        elif coins == 1:
             print("\n" + person + " has " + str(coins) + " coin left.")

        else:
             print("\n" + person + " is out of coins.")

    return play_game #we are not calling the function. we are returning, then we call the parent function


tommy = parent_function("Tommy")
jenny = parent_function("Jenny")

#coin values will change in the scope, closure is created when the parent function is "returned"
tommy()
tommy()
jenny()

tommy() # will run out of coins

print(" ")

#showing the same applies to a parameter

def parent_function2(person, coins):
    #coins = 3

    #parent function returns the play_game() function
    # then the play_game() function has access to the scope of the parent function.

    def play_game2():
        nonlocal coins 
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")

        elif coins == 1:
             print("\n" + person + " has " + str(coins) + " coin left.")

        else:
             print("\n"+ person + " is out of coins.")

    return play_game2 #we are not calling the function. we are returning, then we call the parent function


tommy = parent_function2("Tommy", 3)
jenny = parent_function2("Jenny", 5)

#coin values will change in the scope, closure is created when the parent function is "returned"
tommy()
tommy()
jenny()

tommy() # will run out of coins
