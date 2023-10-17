# dictionaries used to store data values that are in key data pairs
#look a lot like javascript objects

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)


print(type(band))
print(len(band))

#access items in a dictionary
#use the key
print(band["vocals"])
#use method
print(band.get("guitar"))

#list all keys
print(band.keys())

#list all values
print(band.values())


#list of key/value pairs as tuples
print(band.items())

#verify a key exist in dictionary
print("guitar" in band)
print("triagnle" in band)


#change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

#remove items
print(band.pop("bass")) # will remove JPJ
print(band)

band["drums"] = "Bonham"
print(band)

#popitem removes the last key value pair that was added to the dictionary
print(band.popitem()) # will return a tuple
print(band)

#delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)


#empty out a dictionary
band2.clear()
print(band2)

#del entire dictionary
del band2

#copying dictionaries

#how not to copy dictionaries

# #create new band2
# band2 = band # creates a reference in memory, if you make changes they will apply to both
# print("Bad copy!")
# print(band2)
# print(band)

# #add drums to band

# band2["drums"] = "Dave"

# #print band to show changes apply to both
# print(band)


#correct copy

band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band2) # changes only applied to band2
print(band)

# Use dict() constructor function to copy
band3 = dict(band)
print("good copy")
print(band3)

# Nested dictionaries
# this means that the vaule for a key can be another dictionary

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}

member2 = {
    "name": "Page",
    "instrument": "guitar"
}

print(" nested ")
#nested dictionary
band = {
    "member1": member1,
    "member2": member2
}
print(band)

#get a specific value from nested dictionaries
#member1 is going into the dictionary and calling the dictionary member1
#we then use name to call the name of that item
print(band["member1"]["name"])


#can use . notation to view all different methods
#band.

# SETs

# create a set
nums = {1, 2, 3, 4}

#create a set using the constructor function
nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)

print(type(nums))
print(len(nums))


#no duplicates are allowed in sets
nums = {1, 2, 2, 3}

print(nums) #output is a set without duplicates, will not throw error, will ignore the dupelicate

#True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums) # will show first listed and remove the duplicates)

#check if value is in set
print( 2 in nums)


#but you cannot refer to an element in the set with an index position or key

# add a new element to a set

nums.add(8)
print(nums)

#add elements from on set to another
morenums = {5, 6, 7}

nums.update(morenums)
print(nums)

#you can use update with list lists, tuples, and dictionaries


# merge two sets to create a new set
one = {1, 2, 3}
two = {5, 6, 7}

# use union function to merge one and two
mynewset = one.union(two)
print(mynewset)


# keep only the duplicates from the two sets
one = {1, 2, 3}
two = {2, 3, 4}

# like a join will only include duplicates of one and two
one.intersection_update(two)
print(one)  #should only return 2 and 3

# keep everything except duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one) #will only return 1 and 4