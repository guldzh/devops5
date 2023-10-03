

print("Enter two numbers belwo taht are equal:")
num1=int(input("Enter Number 1: "))
num2=int(input("Enter Number 2: "))

if num1==num2:
    print("You entered two equal numbers.")
elif num1!=num2:
    print("You entered two different numbers.")

# By suing elif statemnt we are telling python that both conditions cant be true, 
# so if the first condition is True it does not check th elif's conditions. 