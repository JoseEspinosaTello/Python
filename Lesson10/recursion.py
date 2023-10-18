#Recursion happens in python when a function calls itself
# a recursive function

def add_one(num):

    if(num >= 9):
        return num +1
    # will not return the number 10
    
    total = num + 1 # this will only happen if number is less than 9
    print(total) # prints only 1 - 9

    return add_one(total) # this is the recursive call to the function it calls itself
    # return will reutrn total to the function, will continue to call itself until >= 9 when it just returns num + 1

add_one(0) # will call function until it reaches 9 but will not print 10 as there is no print

# print 10
# once all of the recursive calls the retunr of the if statement is executed

mynewtotal = add_one(0)
print(mynewtotal) # this prints the return of the if statment.

#recursion is a mathematical component and is somtimes needed