"""
Program to enclose all vowels with round braces in a string input by user.
"""


vowels = "aeiouAEIOU"
result = ""

a = input("Enter a string: ") 
for char in a:
    if char in vowels:
        result += "(" + char + ")"
    else:
        result += char
        

print(result)        