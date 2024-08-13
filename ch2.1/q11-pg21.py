"""
The last program can also be worked around with a tuple instead of a list.
This is how:

Since tuples are immutable (i.e., their elements cannot be changed after creation), 
you can't directly sort the tuple. 

However, you can
- Convert the tuple to a list.
- Sort the list.
- Convert the sorted list back to a tuple
"""


myTuple = (15,62,5657,3425,92,2,1909,585,105)

# Convert the tuple to a list for sorting
input_list = list(myTuple)

# Implementing a simple bubble sort algorithm on the list
n = len(input_list)

for i in range(n):
    for j in range(0, n-i-1):
        if input_list[j] > input_list[j+1]:
            # Swap if the element found is greater than the next element
            input_list[j], input_list[j+1] = input_list[j+1], input_list[j]

# Convert the sorted list back to a tuple
sorted_tuple = tuple(input_list)

# Print the sorted tuple
print("Sorted tuple:", sorted_tuple)
