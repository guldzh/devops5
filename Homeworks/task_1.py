quaters=int(input("Please enter the number of Quaters: "))
dimes=int(input("Please enter the number of Dimes: "))
nickels=int(input("Please enter the number of Nickels: "))
pennies=int(input("Please enter the number of Pennies: "))
print(" ")

print("Quaters:",quaters)
print("Dimes:",dimes)
print("Nickels:",nickels)
print("Pennies:",pennies)
print(" ")

quaters_in_cents=quaters*25
dimes_in_cents=dimes*10
nickels_in_cents=nickels*5

amt_in_dollars=(quaters_in_cents+dimes_in_cents+nickels_in_cents+pennies)/100

print(f"The total in dollar is: ${amt_in_dollars}")