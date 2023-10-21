# custom module
from random import choice

capital = "Sacramento"

bird = "California Condor"

flower = "Golden Poppy"

song = "California Love"

def randomfunfact():
    funfact = ["Califorian has a very diverse terrain", "California has 4 NBA teams",
               "When California belonged to Mexico the citizens were called Californios.",
               "I am from California"]
    
    index = choice("0123")

    print(funfact[int(index)])

if __name__ == "__main__":
    randomfunfact() #if we run the california fil it will run the randomfunfact function