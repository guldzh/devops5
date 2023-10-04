user_age = input("Please enter your age: ")
b1= len(user_age)>=2 or len(user_age)>0
b2 = user_age==user_age.lower() and user_age==user_age.upper()
if b1 and b2:
    print("Okay")
else:
   print("Invalid Age!")

