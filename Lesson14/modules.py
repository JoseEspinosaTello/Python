# modules can be considered small code libraries that are based on related features

##modules
import math
#from math import pi
import sys
import random as rdm # we can create an alias and use it to call the module
from enum import Enum #we import only what we need using, in this example we import only Enum form module enum
import california #import custom module
from rps7 import rock_paper_scissors

# access somthing from math
    #print(math.) this will list all the options in the math module, below we selected pi
print(math.pi)
#we are either using functions or constant modules fromt he math module

rdm.choice("123")

#how do we know what to use from a module
# there are a few ways to know what is inside a module

# use the dir function


print(dir(rdm)) 

for item in dir(rdm): # list is hard to read so we loop through it
    print(item) #this doesnt actually tell you what each of these items inside the module does, for this we go to the docs python module index

#use custom module
print(california.capital)
california.randomfunfact()

#one special value that every module has

#the name value
print(__name__)
print(california.__name__)# will get the name of the py file

rock_paper_scissors()