# Create a programm that calculate the grade of the student.
# Ask user their grade in int number and 
#Print A+ if the grade is higher than 95
# Print A if the grade is in between 85 and 94 inclusive.
# print B if the grade is in between 75 and 84 inclusive
# print C if the grade is in between 65 and 74 inclusive. 
# print grade doesn't meet expectations when the grade is lower than 65.

grade=int(input("Please enter your grade: "))
if 100>=grade>=95:
    print("Your grade is A+")
elif 85<=grade<=94:
    print("Your grade is A")
elif 75<=grade<=84:
    print("Your grade is B")
elif 65<=grade<=74:
    print("Your grade is C")
elif 0<grade<65:
    print("Your grade doesn't meet expectations when it is lower than 65")
else: # it is better to use elif when we have multiple conditions. Using else is not recommendened
    print("Not a valid garde!")

