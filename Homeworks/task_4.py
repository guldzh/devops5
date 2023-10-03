# Write a program that will accept 5 digit number 
# and will print reversed number at the end.

user_input=int(input("Please enter any 5 digit number: "))

fifthNum=user_input%10
fourthNum=(user_input//10)%10
thirdNum=(user_input//10//10)%10
secondNum=(user_input//10//10//10)%10
firstNum=(user_input//10//10//10//10)%10

print(f"The output is: {fifthNum}{fourthNum}{thirdNum}{secondNum}{firstNum}")