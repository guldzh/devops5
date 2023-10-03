# Write a Java program to convert minutes into a number of years and days.

minutes=int(input("Enter number of minutes: "))

days_in_a_year=365
minutes_in_a_day=1440

minutes_in_year=int(minutes//(minutes_in_a_day*days_in_a_year))
minutes_in_days=int(((minutes/minutes_in_a_day/days_in_a_year)%minutes_in_year)*365)

print(f"{minutes} minutes is approximately {minutes_in_year} years and {minutes_in_days} days")