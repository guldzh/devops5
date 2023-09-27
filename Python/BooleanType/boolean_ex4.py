stadium_capasity=int(input("Please enter the stadium capasity:"))
amt_ticket_sold=int(input("Please provide the number of sold tickets:"))
ticket_available=int(stadium_capasity - amt_ticket_sold)
is_available=ticket_available>0

print("Can I buy a ticket? -",is_available)