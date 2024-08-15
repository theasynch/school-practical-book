"""
To reverse a 2D array (implemented as a nested list) 
in the order of the 0th element of every inner list, 
you can sort the entire 2D array based on the first 
element of each inner list in descending order. 
Here's how you can implement this in Python:
"""

# Example 2D array (nested list)
array_2d = [
    [3, 2, 1],
    [5, 9, 0],
    [1, 7, 4],
    [4, 6, 8]
]

# Sort the 2D array in reverse order based on the 0th element of each inner list
array_2d.sort(reverse=True, key=lambda x: x[0])

# Print the reversed 2D array
print("Reversed 2D array based on 0th element of each inner list:")
for row in array_2d:
    print(row)
