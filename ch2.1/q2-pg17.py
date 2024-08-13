"""
If the input is "nectarine", output shld be "nctrn"...

Basically to remove all the vowels of the word.
"""


vowels = ["a","e","i","o","u"]

a = input("Enter a string:")

for i in a:
    if i in vowels:
        print(f"The final word without vowels becomes:{a}")