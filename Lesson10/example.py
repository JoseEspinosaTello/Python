#while loops and how the evaluate the true or false condition
# value = True

# while value: #implies while value exists
#     print(value)
#     value = False # will exit the loop


value = "y"
count = 0
while value:
    count += 1
    print(count)
    if (count == 5):
        break
    else:
        value = 0 #this will still end the loop
        continue # when using keyword continue the loop is still evaluated at the top, checking while partd