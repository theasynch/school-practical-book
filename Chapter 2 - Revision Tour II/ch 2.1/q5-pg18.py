"""
Checking if statements are legal or not.
Here, myList, myTuple, and myString are 
any random List, Tuple and String respectively.
"""

#Statement 1

myList = myList+[4] #---------> LEGAL

#Statement 2

myList.append(4) #---------> LEGAL

#Statement 3

del myList[0]  #---------> LEGAL

#Statement 4

myTuple = myTuple + (4,) #---------> ERROR

#Statement 5

myTuple.append(4) #-----------> ERROR

#Statement 6

del myTuple[0] #-----------> ERROR

#Statement 7

myString  = myString+"4" #-------------> LEGAL

#Statement 8

myString.append(4) #-----------> LEGAL

#Statement 9

del myString[0] #----------> LEGAL
