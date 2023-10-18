# Functions: reusable blocks of code

# define function
#namming a function: must be all lower case, underscores and lowercase
def hello_world():
    print("Hello World!")


#call the function
hello_world()

#somtimes we need to use place holders for our data
# this is called parameters 

def sum(num1, num2):
    print(num1 + num2)

#call the function and pass arguments to the parameters

sum(3, 4) 

# the parameters never change however arguments can change everytime the function is called
sum(6, 10)
sum(9, 200)
sum(2, 10)
sum(90, 50)

#returning values
def add(numer1, numer2):
    #check parameters
    if (type(numer1) is not int or type(numer2) is not int):
        return
    return numer1 + numer2

total = add(4, 3) 
total = add("a", 3) # will return none
#total = add() # if nothing is passed in will return error
print(total)

#could assign default values to param
def add2(numer1 = 0, numer2 = 0):
    #check parameters
    if (type(numer1) is not int or type(numer2) is not int):
        return
    return numer1 + numer2

total = add2(4) # when an assigned value to param you can leave it blank or add a value
total = add2(4, 5) 

print(total)

#sum functions may receive multiple arguments but when you are defininf the function you wont know how many arguments are going to be passed into it
def multiple_items(*args): # when we dont know how may arguments we will recieve we will start with *args
    print(args)
    print(type(args))

multiple_items("Dave", "John", "Sara")

#when passing multiple items but want to use keyword arguments
def mult_named_items(**kwargs): #start with **kwargs (keyword arguments)
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = "Dave", last = "Gray")