"""
If the input is "nectarine", output shld be "nctrn"...

Basically to remove all the vowels of the word.
"""


vowels = ["a","e","i","o","u"]

a = input("Enter a string:")
result = [letter for letter in a if letter.lower() not in vowels] 
result = ''.join(result) 
print(result) 
  