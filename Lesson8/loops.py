#while loop
value = 1

# while value <= 10:
#     print(value)
#     if value == 5:
#         break # stops the loop
    
#     value +=1 


# while value <= 10:
   
#     value +=1 
#     if value == 5:

#         continue  #will allow the loop to step threw past 5
#         # the value increment needs to be added before continue otherwise it will become endless loop
#     print(value)

# else:
#     print("value is now equal to:" + str(value))
         
    
#for loop
# for loop iterates a sequence

# create a list
names= ["Dave", "Sara", "John"]

# for x in names:
#     print(x)

# #will iterate threw mississippi and print every letter
# for x in "Mississippi":
#     print(x)


# for x in names:
#     if x == "Sara":
#         break # loop will stop once reaches sara
#     print(x)

# for x in names:
#     if x == "Sara":
#         continue # loop will step threw sara and go to the next iteration of the loop
#     print(x)

# loop that iterates through a range
for x in range(4):
    print(x) # will print 0 - 3 as it starts at index 0

print("Break \n")


for x in range(2, 4):
    print(x) # will start at 2 and stop at 4. will list 2 and 3

    print("Break \n")

# tell range how to increment
#start at 0, go up to 100, increments of 5
for x in range(0, 101, 5):
    print(x)
#can also add else to for loop
else:
    print("Glad that\'s over!")


print("Break \n")

#NESTED FOR LOOPS   
names= ["Dave", "Sara", "John"]
actions= ["codes", "eats", "sleeps"]

# #for each name in list we will do something
# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")


#revers
for action in actions:
    for name in names:    
        print(name + " " + action + ".")

#use loops to improve rock, paper scissors    