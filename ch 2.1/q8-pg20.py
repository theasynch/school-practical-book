a = [[[1,2,3,4,5],[6,7,8]],9] # This is a nested list containing a nested list containing 2 elements.

a[-1] = 200 #Changing the last element of 'a' (i.e 9) to 200

b = a[:]
b[0][0][3] = 17
print(a)
print(b)


"""
No line of this code gives out an error.
"""