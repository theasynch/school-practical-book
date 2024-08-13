"""
If the input is "nectarine", output shld be "n(e)ct(a)r(i)n(e)"...

Basically, enclose all vowels with braces
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