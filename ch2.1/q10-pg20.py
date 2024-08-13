"""
Program to sort integers of an array into ascending order.
Program uses a bubble sort algorithm.
"""


"""
An array is essentially a list datatype that contains only integer datatype elements.
An array is synonymous to matrices in mathematics.
"""

myList = [15,62,5657,3425,92,2,1909,585,105] #This is an arbitrary list. You can use any other array as you like.

# Implementing a simple bubble sort algorithm
n = len(myList)

for i in range(n):
    for j in range(0, n-i-1):
        if myList[j] > myList[j+1]:
            # Swap if the element found is greater than the next element
            myList[j], myList[j+1] = myList[j+1], myList[j]

# Print the sorted list
print("Sorted list:", myList)