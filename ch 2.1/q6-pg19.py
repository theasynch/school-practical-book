a = [1,2,3]
a[2] = 0

a[a[2]] = 5
a[1:2] = []

print(a)

"""
The code yields [5, 0] as the final value of 'a'
"""