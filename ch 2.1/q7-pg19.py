list = [] #Creating an empty list.

a = input("Enter a string: ") #Accepting a string from the user

for i in a:
    list.append(i) #Slicing the string and then adding its elements to the list

list.remove(list[0]) #Removing the first element of the string from the created list

print(f"The entered string was{a}.\n This converted to a list and first element removed is {list}") #printing the final list.

