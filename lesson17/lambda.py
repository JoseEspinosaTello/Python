#lambda function is a single expression that returns a key value
#cant call call lambda by name because it is ananymous

def squared(num): return num * num
#lambda num : num * num 
print(squared(2))


def addTwo(num): return num + 2
#addtwo = lambda num : num + 2

print(addTwo(12))

def sum_total(a, b): return a + b
#sum = lambda a, b : a + b

print(sum_total(10, 8))


#################################################

#lambda is most often used inside of another function when you need a quick function

def funcBuilder(x):
    return lambda num : num - x

#now use this function to build other functions

addTen = funcBuilder(10) # 10 is passed to the x param in the functions
addTwenty = funcBuilder(20) # function then returns the lambda which can accept another param

print(addTen(7)) # passing param to lambda
print(addTwenty(7))# lambda will receive this number in the num variable


#High oder function
# a function that takes one or more functions as a arguments or a function that returns a function as its result.




numbers = [3, 7, 12, 18, 20, 21]

#map() is a function build into python that receives a function as a first argmuent
# map second argument is a data collection (list)
squared_nums = map(lambda num : num * num, numbers)

#now we use the list contructor to create a new list
print(list(squared_nums))


##########################################################
lambda num : num % 2 != 0 # this lambda will return try or false as it is a comparison


odd_nums = filter(lambda num : num % 2 != 0, numbers) # will return the number from the list that are odd
# filters out everything that did not return True

print(list(odd_nums))

###########################################################

from functools import reduce

#reduce can be a complex function but it simply adds everything together

#function that reduce accepts needs to parameters
# the first is an accumulator
# second is a current which represents the current item,

lambda acc, curr: acc + curr

numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers, 10) #10, is a starting value

print(total)



print(sum(numbers, 10)) #sum also accepts a starting number

lambda acc, curr : acc + len(curr)

names = ['Dave Gray', 'Sara Ito', 'John Jacob Jingleheimerschmidt'] 

#we are going to use reduce to add all the characters together and get a total

char_count = reduce(lambda acc, curr : acc + len(curr), names, 0) 
print(char_count)