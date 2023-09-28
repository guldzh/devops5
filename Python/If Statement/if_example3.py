# Create a programm that calculate the grade of the student.
# Ask user their grade in int number and 
#Print A+ if the grade is higher than 95
# Print A if the grade is greater 

grade=int(input("Please enter your grade: "))
if grade>=95:
    print("Your grade is A+")
elif 85<=grade<=94:
    print("Your grade is A")
elif 75<=grade<=84:
    print("Your grade is B")
elif 65<=grade<=74:
    print("Your grade is C")
elif 0>grade or grade>100:
    print("Not Valid Grade!")
else:
    print("Your grade doesn't meet expectations when it is lower than 65")

