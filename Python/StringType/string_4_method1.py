s="techtorial"
print(s.upper())

print(s)  # Immutable data types will not change the original value unless reassigned 

# When do we call it function  or method?
# when a belongs to certian data type then we call it only method
# however when it can be used independently than we call it a function

s2="TechTorIaL"
print(s2.lower())

user_age = input("Please enter your age: ")
int_age=int(user_age)
if len(int_age)>=3:
    print("Invalid Age!")
else:
    print("Okay")