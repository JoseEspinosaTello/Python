#print(x) # we havent defined x and python will throw an exception

#custom exceptions start with class
class JustNotCoolError(Exception): 
    pass 

#w3schools will list the built in python exceptions that can be raised.
x = 2
try:
    raise JustNotCoolError("This just isnt cool, man.")
    #raise Exception("I'm a custom exception!") #dont often see a generic exception, often the exceptions are named to specify what we expect the exception to be 
   # print(x / 0)
#    if not type(x) is str: 
#        raise TypeError("Only strings are allowed.")
except NameError: #NameError will not catch division error
    print('NameError means something is probably undefined.')

except ZeroDivisionError: #create another exception to catch division error
    print('Please do not divide by 0.')

except Exception as error:
    print(error)
else: # only happens if there are no exception
    print('No errors!')
finally: #finally will print no matter what
    print("I'm going to print with or without an error.")