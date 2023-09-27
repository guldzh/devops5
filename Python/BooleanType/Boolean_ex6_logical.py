# Multiple of 3 and 5
# Write a program that takes a number as input and prints
# True if the number is a multiple of both three and five, False otherwise.

number=int(input("Please enter some number: "))
#If the number is divisible by number there should not be remainder
is_divisible_3=number%3 ==0
is_divisible_5=number%5 ==0
# or we can do "is_divisible_3=number%3 ==0 and is_divisible_5=number%5 ==0"

print(is_divisible_3 and is_divisible_5)

