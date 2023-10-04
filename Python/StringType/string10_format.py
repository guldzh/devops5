# Formating is sort of a short cut to embed values from other data types in to string
# There is two ways we could format string. 
# *1 usinf format method.
# ex: We will put the curly braces in a string, 
# and those curly braces will be replaced by an argument that we puy in a format method

s = "Today weather is {} farenheit."
print(s) # will print -> "Today weather is {} farenheit."

print(s.format(84)) #will print -> "Today weather is 84 farenheit."
print(s.format("eighty four")) #will print -> "Today weather is eighty four farenheit."

# Note! We could youse more than one curly brace to format the strings, 
# as well as using index for curly brances
# age=input("Enter your age: ")
# name=input("Enter your name: ")
# s2="My name is {} and my age is {}"
# print(s2.format(name, age))

# brand=input("Enter your laptop brand: ")
# model_year=input("Enter your model year: ")
s3="The brand of the laptop is {1}, and model year is {0}"
print(s3.format(2019, "Linux"))
