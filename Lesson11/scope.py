#global scope

# if we create variable it is in the global scope as it is availble to everything in the file

name = "Dave"

#create a function

# def greeting(firstname): # this parameter has the same name as the variable but it is not the same scope and therefore not the same item
#     color = "blue" # defined inside the function so scope is in the local scope of the function. cannot call in global scope
#     print(color)
#     print(name)
#     print(firstname) # using var name in this situation it will print dave as it is a globale function

# greeting("John")

# def greeting(name): # this parameter has the same name as the variable but it is not the same scope and therefore not the same item
#     color = "blue" # defined inside the function so scope is in the local scope of the function. cannot call in global scope
#     print(color)
#     print(name)
   
# greeting("John")

# print("\n")
# def another():
#     greeting("Dave")

# another()


# #define functions inside another function
# def another(): # this parameter has the same name as the variable but it is not the same scope and therefore not the same item
#     color = "blue" # defined inside the function so scope is in the local scope of the function. cannot call in global scope

#     def greeting(name):
#         print(color)
#         print(name)
  
#     greeting("Dave")


# another()

#overall you try to keep the global scope as clean as possible as poluting the golbal scope can cause issues


#what if we want to modify the assignment of a variable inside the function but the variable was defined in the global scope

count = 1 #global


def another():
    color = "blue" 
    #count = 2 # will result in 2 as will use the local variable for value
    #use the global count with the global keyword
    global count
    count += 1
    print(count) 
    def greeting(name):
        nonlocal color
        color = "red"
        print(color)
        print(name)
  
    greeting("Dave")


another()
