person = "Dave"
coins = 3

print("\n" + person + " has " + str(coins) + " coins left.")

#older ways to format strings

message = "\n%s has %s coins left." % (person, coins) # will put person where the first % is and coins where the second %is

print(message)


#using format method / brackets 
message = "\n{} has {} coins left.".format(person, coins) 

print(message)

#using formate method but using index number to say wich position of the value is going in
message = "\n{1} has {0} coins left.".format(coins, person)  # position resverse as previous because index starts with 0.

print(message)


#using formate method but refering them as the names that they have
message = "\n{person} has {coins} coins left.".format(coins = coins, person = person)  # position resverse as previous because index starts with 0.

print(message)


# creat a dictionary

player = {'person': 'Dave',
          'coins': '3'}


message = "\n{person} has {coins} coins left.".format(**player)  # use ** to pull in values from dictionary based on what we have assigned the keys. Person will return value, and coin will return value.

print(message)


#with these formats the more values we pass in the long the string is.

#f_Stings can help us shorten this out

#f_string this is the way

message = f"\n{person} has {coins} coins left." # not as verbose

print(message)

message = f"\n{person} has {2 * 5} coins left." # can use operators and pass in an equation as well

print(message)

message = f"\n{person.lower()} has {2 * 5} coins left." # can use methods as well.

print(message)


message = f"\n{player['person']} has {2 * 5} coins left." # can use dictionaries as well need to use single quotes for the key.

print(message)

# pass formatting options into the f_strings

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}") #number will be 2 decimal places over and f means fixed point

# put f_string in loop

for num in range(1,11):
    print(f"\n2.25 times {num} is {2.25 * num:.2f}") # will give us the result of each value in the range


for num in range(1,11):
    print(f"\n{num} divided by 4.52 is {num / 4.52:.2%}") 

#use w3schools f_string format