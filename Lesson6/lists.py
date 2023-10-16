users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptylist = []

print("Dave" in data)
print("Dave" in emptylist)

print(users[0])
print(users[-1]) #find last value in list
print(users[-2]) 

print(users.index('Sara')) # return position of sara

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

# add more items to list
users.append('Elsa')
print(users)

# add a list to another list

users += ['Jason']
print(users)

# another way to combine lists
users.extend(['Robert', 'Jimmy'])
print(users)

# add data list to users list
# users.extend(data)
# print(users)

# add items to beginning of the list
# 0 is the index position
users.insert(0, 'Bob')
print(users)

# this will not replace the other values because we are saying start and end at the same position
users[2:2] = ['Eddie', 'Alex']
print(users)

# replace valuses
# this is a slice and will replace the the values
users[1:3] = ['Robert', 'JPJ']
print(users)


# remove data from lists

users.remove('Bob')
print(users)

# can pop off the last user from list
# pop method will return the value removed

print(users.pop())
print(users)

#delete users
#will remove Robert as he is index 0

del users[0]

#delete data entirely
# del data
# print(data)

# this just deletes the data in the list, list still exists
data.clear()
print(data)

# when we insert a lower cast item it goes to the end of the list
# this will replace Alex as well as it is a slice
users[1:2] = ['dave']
users.sort()
print(users)

# insert dave in first position
# this will sort in alphabetical order
users.sort(key=str.lower)
print(users)

#numbers lists
nums = [4, 42, 78, 1, 5]

#revese the list as ascending
nums.reverse()
print(nums)

#revers as descending
# nums.sort(reverse=True)
# print(nums)

# keep list as it was, but sort the list for and individual purpose.
# this returns the same list as above but does not modify the original list
#using global sorted function
print(sorted(nums, reverse=True))
print(nums) # print list to show the original list has not changed

# copy
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:] # slice full list and store it in the copy of list


print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

#change type of list

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)

# Tuples
# are like lists except the data inside Tuples will not change and the order will not change
# use parentheses () instead of brackets []
#Create tuple with constructor
mytuple = tuple(('Dave', 42, True))

#create tuple without constructor
anothertuple = (1,4,2,8,2,2)

print(mytuple)

print(type(mytuple))
print(type(anothertuple))

# tuples can be copied
# packing the tuple is assigning values to a tuple
# to pack a tuple you need to get creative

# create a list using the old tuple
newlist = list(mytuple)

#append a new value to the tuple
newlist.append('Neil')

#create a new tuple using the updated list
newtuple = tuple(newlist)

# new tuple with new value
print(newtuple)


# unpacking a tuple
# can be unpacked into new variable names

(one, two, *hey) = anothertuple
print(one)
print(two)
print(hey)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

# we can check what methods are availble on list or tuple

#will count how many occurances of the number 2
print(anothertuple.count(2))