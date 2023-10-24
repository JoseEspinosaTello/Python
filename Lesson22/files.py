import os
# working with files in python

# r = Read
# a = Append 
# w = Write
# x = Create

# Read - error if it doesnt exist

f = open("names.txt")
# print(f.read())
# print(f.read(4)) # read the first 4 characters of the file

# print(f.readline()) #read first line of the file
# print(f.readline()) #when run again it will read the next line

for line in f: # will loop and print each line
    print(line)

f.close() # should always close file after opening, important because if you change a file the change will not take place until it is closed


# what we should do to avoid an error
# use a try black

try:
    # f = open("name_list.txt") # will throw error because this file does not exist
    f = open("names.txt")
    print(f.read())
except:
    print("The file you want to read doesn't exist")
finally:
    f.close()


# Append - creates the file if it doesnt exist

f = open("names.txt", "a")
f.write("\nNeil")
f.close()

f = open("names.txt")
print(f.read())
f.close()


# Write (overwrite everything in the file)

f = open("context.txt", "w")
f.write("I deleted all of the context")
f.close()

f = open("context.txt")
print(f.read())
f.close()

#two ways to create a new file

# Opens a file for writing, also creates the file if it does not exist.

f= open("name_list.txt", "w") # if doesnt exist you will see an new file
f.close()

# Creates the specified file, but returns an error if the fil exists.

if not os.path.exists("dave.txt"):
    f = open("dave.txt", "x") # "x" means create
    f.close()

# Delete a file

# avoid an error if it doesnt exist

if os.path.exists("dave.txt"):
    os.remove("dave.txt")
else:
    print("The file you wish to delete does not exist")


# work with files not using try except finally

# open the more_names file
with open("more_names.txt") as f: # f represents the file
    content = f.read()

#write the more_names content to the names.txt file
with open("names.txt", "w") as f:
    f.write(content)