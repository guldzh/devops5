# input function allows us to work with dynamic values because 
#values will be given by user when the code runs
#Input function will always give the data as text(string), 
#so we would convert it acording what we need using functions like (int(), float(), bool())

#Example;
var1=int(input("Enter your age:"))
print("The user's age is",var1) #This will print usersinput
print(type(var1)) # Type will be <class 'str'> (text)

# Print True if the users' age is older than 25, print false if otherwise

is_older=var1>21
print("User is is older than 21? ",is_older)