"""
Program to remove vowels from a string entered by an user.
"""


vowels = "aeiouAEIOU"

a = input("Enter a string:")
result = [letter for letter in a if letter.lower() not in vowels] 
result = ''.join(result) 
print(result) 
  