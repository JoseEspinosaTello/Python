#string data type

#literal assignment
first = "Dave"
last = "Gray"

#print the datatype
print(type(first))

print(type(first) == str)

print(isinstance(first, str))

#Constructor function
pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))


#Concatentation: adding two string together to make a single string

fullname = first + " " + last

print(fullname)

#add to the value of fullname

fullname += "!"
print(fullname)

#casting a number to a string
#to use a number as a string we first need to convert it to a string.
decade = str(1980)

print(type(decade))
print(decade)

statement = "I like rock musing from the " + decade + "s."

print(statement)

#multiple lines
multiline = '''
Hey, how are you?

I was just checking in.
                            All good?
'''

print(multiline)

# Escaping special characters
#VScode doesnt like when the single quote is used in the word "I'm"
#vscode see it as the quote ending
# you add the \ before the single quote in the word I'm  to escape the special character
#\t is used to tab
#\n is used to start a new line
# \\ is used to escape a single \ in the sentence 
sentance = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentance)

# String Methods: string functions that are called on the string class
#shift + ALT + down arrow copies the code one line down

print(first)
print(first.lower()) # makes all lowercase
print(first.upper()) # makes all uppercase
print(first) # shows the acual value is untouched. The method applies the change.

print(multiline.title()) # this capitalizes the first letter in every word

print(multiline.replace("good", "ok")) # replace word good with ok.
print(multiline)

# chech lenght of multine
print(len(multiline))

#add whitespace to the end of the line
multiline += "                                                       "

# add whitespace to the front of multiline
multiline = "                    " + multiline


# check lenth after changes
print(len(multiline))

#string methods that remove whitespace

print(len(multiline.strip())) # remove all whitespace
print(len(multiline.lstrip())) # remove whitespace left side
print(len(multiline.rstrip())) #remove whitespace right side

# Build a menu

#create title variable and make all upper case using method
title = "menu".upper()

#print title but center it inbetween 20 equal signs
print(title.center(20, "="))
#word coffee is placed to the left of all periods
#we concatenate the price right justified which will be set after 4 spaces of white space.
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))
print("")

#string index values
print(first[1]) # prints second letter in name

print(first[-1]) #gives last value in string

#give a range of values
print(first[1:]) #provide a value without providing the final value


# some methods return boolean data
print(first.startswith("D")) #string first does start with D
print(first.endswith("Z")) #false string does not end with Z

# Boolean data type

myvalue = True

x = bool(False)

print(type(x))

print(isinstance(myvalue, bool)) # will return true if the value is boolean


# numeric datatypes

#integer

price = 100

bestprice = int(80)

print(type(price))

print(isinstance(bestprice, int)) # will return true if the value is int


# float type

gpa = 3.28

y = float(1.14)
print(type(gpa))

#complex type used in eletrical engineering

comp_value = 5 + 3j

print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# built-in functions for numbers

print(abs(gpa)) # absolute value
print(abs(gpa * -1))

print(round(gpa)) # round the number to the nereast integer

print(round(gpa, 1)) # this will round to the nearest decidmal place that we specify

# import math module with provide many good mathmatic helpers
import math 

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))


# Casting a string to a number

zipcode = "10001"

zip_value = int(zipcode)

print(type(zip_value))

# can have an error if you attempt to cast incorrect data

#zip_value = int("New Yourk") this will be an error
