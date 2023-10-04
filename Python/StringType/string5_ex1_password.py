# Ask user to enter the password but there will be conditions, 
# our condition for a valid password is: 
# 1. It has to have a upper case 
# 2. it has to have a lower case
# If user provides a valid password print "your password is valid"
# Othervise print your passowrd is invalid

user_input=input("Please provde a passowrd: ")
if user_input == user_input.lower() or user_input == user_input.upper():
    print("Please provide a valid password")
else:
    print("Your password is valid")


user_age = input("Please enter your age: ")
int_age=int(user_age)
if len(int_age)>=3:
    print("Invalid Age!")
else:
    print("Okay")  