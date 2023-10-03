# Write a program that will take a given amount of 
# money and return the number of dollars in quarters, dimes, nickels, and pennies 
# that make up that given amount

balance=float(input("Please enter your balance: "))
balance_in_pennies=balance*100

quaters=int(balance_in_pennies//25)
rest_from_quaters=balance_in_pennies-(quaters*25)

dimes=int(rest_from_quaters//10)
rest_from_dimes=rest_from_quaters-(dimes*10)

nickels=int(rest_from_dimes//5)
pennies=int(rest_from_dimes-(nickels*5))

print(f"${balance} will make: {quaters}-quater(s), {dimes}-dime(s), {nickels}-nickel(s) and {pennies}-pennie(s)")
