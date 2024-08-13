"""
Program to define two tuples and then creating a new third one
that contains all the elements from the first two.
"""


myTuple1 = (1,3,5,6)
myTuple2 = ("Hello", "World", "Python", "Programming") 

#The above two tuples are arbritary. Feel free to use any other tuples as you like.

myTuple3 = tuple(myTuple1 + myTuple2) #Defining a new myTuple3, adding the elements and then converting its datatype.

print(myTuple3)