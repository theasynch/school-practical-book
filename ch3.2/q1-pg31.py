"""
Given below is a sample function. 
The question asks us to identify the different parts of the function.
"""

def lastDigitCube(n):
    d = n%10
    c= d**3
    return c


number = int(input("Enter a number: "))
cube = lastDigitCube(number)
print("The cube of its last digit is", cube)


"""
a) Function Header : lastDigitCube
b) Name and number of arguments : One, "n"
c) Number of statements in the function body : 3
d) Number of statements in the main program : 4
e) Function call statement : lastDigitCube()
f) Parameters' Name : 
g) Arguments' Name : "n"

h) Flow of execution : main.6 >> main.13 >> fn.1 >> fn.2 >> fn.3 >> main.8
"""