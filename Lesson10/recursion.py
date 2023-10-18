#Recursion happens in python when a function calls itself
# a recursive function

def add_one(num):

    if(num >= 9):
        return num +1
    
    total = num + 1 # this will only happen if number is less than 9
    print(total)

    return add_one(total) # this is the recursive function it calls itself
    # will continue to call itself until >= 9 when it just returns num + 1

add_one(0) # will call function until it reaches 9 but will not print 10 as there is no print