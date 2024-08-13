myTuple=(1,2,3)
myTuple.append(4)
print(myTuple)

"""
The above code will throw an error since a tuple
is an immutable object and 'append' is not one of its attributes.
"""

myTuple2 = (1,2,3)
myTuple3=(4)
print(myTuple2+myTuple3)

"""
The above part of the code will show no error and will simply print 
1,2,3,4
since it only contains printing an addition of the elements of the both tuple.
"""


myList=[0,3,4,1]
myList.remove(3)
print(myList)

"""
The above code will show no error since list is a mutable object.
The code simply removes '3' from the list and prints the remaining elements.
"""
