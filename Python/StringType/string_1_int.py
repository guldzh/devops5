#   Ask user to enter string
# print the length of the given string, and print the 5th letter from the string

user=input("Please enter some word mre than 5 chars: -> ")

if len(user) >= 5:
  print(user[4])
else:
  print("Please enter word more than 5 chars!")